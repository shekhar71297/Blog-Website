from django.shortcuts import render

all_posts=[
    {
        'slug':'animal-diary',
        'image':'b6.jpg',
        'posted_by':'abc',
        'date':'11/11/11' ,
        'title':'Bird',
        'extract':'xyz',
        'Author':'harry',
        'content':'This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.'
    },
    {
        'slug':'tech-nology',
        'image':'b3.jpg',
        'posted_by':'abc',
        'date': "12/12/12",
        'title':'technology',
        'extract':'abc',
        'Author':'harry',
        'content':'This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.'
    },
    {
        'slug':'sport-game',
        'image':'b5.jpg',
        'posted_by':'abc',
        'date': "12/12/12",
        'title':'sport',
        'extract':'abc',
        'Author':'harry',
        'content':'This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.'
    },
    {
        'slug':'travel-diary',
        'image':'b2.jpg',
        'posted_by':'abc',
        'date': "12/12/12",
        'title':'traveling',
        'extract':'travel',
        'Author':'harry',
        'content':'This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.'
    }
]

# Create your views here.
def HomePage(request):
    limited_post=all_posts[:3]
    return render(request,'blogwebapp/Home.html',{
        'posts_data': limited_post
    })

def AboutPage(request):
    return render(request,'blogwebapp/about.html')

def PostPage(request,slug):
    return render(request,'blogwebapp/Allpost.html',{
        'posts_data': all_posts
    })

def PostDetails(request,slug) :
    identified_slug=next(post for post in all_posts if post['slug']==slug )
    return render(request,'blogwebapp/postdetails.html',{
            'posts_data':identified_slug
    })

