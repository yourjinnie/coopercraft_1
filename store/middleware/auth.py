from django.shortcuts import redirect
# from django.urls import reverse

def auth_middleware(get_response):
    def middleware(request):
        returnUrl = request.get_full_path()
        if not request.session.get('user'):
            return redirect(f'/account?return_Url={returnUrl}')
        response = get_response(request)
        return response
    return middleware






# return redirect(f'account?return_Url={returnUrl}')
# def auth_middleware(view_function):
#     def wrapped_view(request, *args, **kwargs):
#         if not request.user.is_authenticated:
#             next_url = request.get_full_path()
#             login_url = f"{reverse('account')}?next={next_url}"
#             return redirect(login_url)
#         return view_function(request, *args, **kwargs)
#     return wrapped_view
