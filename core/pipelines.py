from core.models import Profile

# OAuth pipeline element that extends User model (Profile)
# Takes extra data(like location, avatar url....) from OAuth Backend and saves to Profile model
def extend_user_data(backend, user, response, *args, **kwargs):
    if backend.name == 'gitlab':
        try:
            profile = user.profile 
        except Profile.DoesNotExist:
            profile = Profile(user=user)

        profile.profile_url = response.get('web_url')
        profile.avatar_url = response.get('avatar_url')
        profile.location = response.get('location')
        # Service user id (like GitLab user id)
        profile.suid = response.get('id')

        profile.get_projects(response.get('access_token'))
        profile.save()

