def unauthenticated_user(view_func):
    def wrapped_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
            # return redirect('home')
        return view_func(request, *args, **kwargs)

    return wrapped_func


def allowed_users(should_be_teacher):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.is_teacher == should_be_teacher:
                return view_func(request, *args, **kwargs)
            else:
                pass
                # return redirect('home')

        return wrapper_func

    return decorator
