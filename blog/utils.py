from .models import Post

def get_page(request):
    page = request.GET.get('page', '') 
    if not page:
        page = 1 
    return page
def prev_next_post(id):
    id = int(id)
    prev_id = id - 1 
    next_id = id + 1 
    try:
        prev_post = Post.objects.get(pk=prev_id)
    except:
        prev_post = None
    try:
        next_post = Post.objects.get(pk=next_id)
    except:
        next_post = None
    return prev_post,next_post
