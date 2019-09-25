from django.shortcuts import render
try:
    from .insta_parser import insta_items, insta_items_details
except:
    pass

# Create your views here.

def galery(request):
    context = {
        'insta_items': insta_items,
    }
    return render(request, 'gallery/galery.html', context)


def insta_details(request, id):
    for i in range(len(insta_items_details)):
        if id in insta_items_details[i]:
            post = insta_items_details[i]
            if i == len(insta_items_details)-1:
                next_post = None
            else:
                next_post = insta_items_details[i+1]
            if i == 0:
                prev_post = None
            else:
                prev_post = insta_items_details[i-1]
    url = post[0]
    text = post[1]
    likes = post[3]
    comments = post[2]
    comments_list = post[6]
    days_from_post = post[7]
    link = post[4]
    if next_post:
        next_id = next_post[5]
    else:
        next_id = False
    if prev_post:
        prev_id = prev_post[5]
    else:
        prev_id = False

    context = {
        'url': url,
        'text': text,
        'next_id': next_id,
        'prev_id': prev_id,
        'comments_list': comments_list,
        'likes': likes,
        'comments': comments,
        'days_from_post': days_from_post,
        'link': link,
    }

    return render(request, 'gallery/insta_details.html', context)

