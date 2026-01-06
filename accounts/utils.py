def can_access_dashboard(user):
    if not user.is_authenticated:
        return False

    if not user.is_approved:
        return False

    # SYSTEM LEVEL
    if user.system_role in ["admin", "management"]:
        return True

    # PROFILE LEVEL
    if hasattr(user, "profile"):
        if user.profile.profession in ["staff", "instructor"]:
            return True

    return False
