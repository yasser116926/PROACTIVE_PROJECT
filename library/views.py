from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404

from .models import LibraryResource
from .forms import LibraryResourceForm
from django.http import JsonResponse


# =========================
# Permissions
# =========================
def is_staff_user(user):
    return user.is_authenticated and user.is_staff


# =========================
# Dashboard Upload
# =========================
@method_decorator(user_passes_test(is_staff_user), name='dispatch')
class LibraryResourceUploadView(View):
    def get(self, request):
        form = LibraryResourceForm()
        return render(request, "dashboard/upload_library.html", {"form": form})

    def post(self, request):
        form = LibraryResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploaded_by = request.user
            resource.save()
            return redirect("dashboard-home")
        return render(request, "dashboard/upload_library.html", {"form": form})

class ResourceListView(ListView):
    model = LibraryResource
    template_name = "library/library_list.html"
    context_object_name = "resources"
    ordering = ["-created_at"]
    paginate_by = 10

class ResourceDetailView(DetailView):
    model = LibraryResource
    template_name = "library/library_detail.html"
    context_object_name = "resource"

class MyLibraryResourcesView(ListView):
    model = LibraryResource
    template_name = "library/my_library_resources.html"
    context_object_name = "resources"
    ordering = ["-created_at"]

    def get_queryset(self):
        return LibraryResource.objects.filter(
            uploaded_by=self.request.user
        ).order_by("-created_at")

            


# =========================
# Public Views
# =========================
def library_list(request):
    resources = LibraryResource.objects.all().order_by("-created_at")
    return render(request, "library/library_list.html", {"resources": resources})


def library_detail(request, pk):
    resource = get_object_or_404(LibraryResource, pk=pk)
    return render(request, "library/library_detail.html", {"resource": resource})


def library_resource_download(request, pk):
    resource = get_object_or_404(LibraryResource, pk=pk)
    if resource.book_pdf:
        return redirect(resource.book_pdf.url)
    raise Http404("No file available")


# =========================
# User Views
# =========================
@login_required
def my_library_resources(request):
    resources = LibraryResource.objects.filter(
        uploaded_by=request.user
    ).order_by("-created_at")
    return render(request, "library/my_library_resources.html", {"resources": resources})


# =========================
# Edit / Delete
# =========================
@user_passes_test(is_staff_user)
def edit_library_resource(request, pk):
    resource = get_object_or_404(LibraryResource, pk=pk)

    if request.method == "POST":
        form = LibraryResourceForm(request.POST, request.FILES, instance=resource)
        if form.is_valid():
            form.save()
            return redirect("library-detail", pk=resource.pk)
    else:
        form = LibraryResourceForm(instance=resource)

    return render(
        request,
        "dashboard/edit_library.html",
        {"form": form, "resource": resource},
    )


@method_decorator(user_passes_test(is_staff_user), name="dispatch")
class LibraryResourceDeleteView(DeleteView):
    model = LibraryResource
    template_name = "dashboard/confirm_delete_library.html"
    success_url = reverse_lazy("library-list")


# =========================
# Pagination & Search
# =========================
def paginated_library_list(request):
    resources = LibraryResource.objects.all().order_by("-created_at")
    paginator = Paginator(resources, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "library/paginated_library_list.html",
        {"page_obj": page_obj},
    )


def search_library_resources(request):
    query = request.GET.get("q", "")
    results = LibraryResource.objects.filter(
        Q(subject__icontains=query)
        | Q(formulas_text__icontains=query)
        | Q(external_links__icontains=query)
    ).order_by("-created_at")

    return render(
        request,
        "library/search_results.html",
        {"results": results, "query": query},
    )





def library_resources_api(request):
    resources = LibraryResource.objects.all().order_by('-created_at')

    data = []
    for r in resources:
        data.append({
            "id": r.id,
            "subject": r.get_subject_display(),
            "book_pdf": r.book_pdf.url if r.book_pdf else None,
            "question_bank_pdf": r.question_bank_pdf.url if r.question_bank_pdf else None,
            "formulas_text": r.formulas_text,
            "diagrams_images": r.diagrams_images.url if r.diagrams_images else None,
            "external_links": r.external_links,
        })

    return JsonResponse(data, safe=False)
