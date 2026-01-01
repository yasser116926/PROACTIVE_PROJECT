# accounts/utils.py

def can_approve(approver_profile, target_role):

    if approver_profile.role == 'ADMIN':
        return True

    if approver_profile.role == 'MANAGEMENT':
        return target_role in ['INSTRUCTOR', 'STUDENT']

    if approver_profile.role == 'INSTRUCTOR':
        return target_role == 'STUDENT'

    return False
