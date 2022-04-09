
from datetime import date
from urllib import request
from django.shortcuts import render

# Create your views here.
#dummy data
all_posts =[
    {
        "slug":"mountainhiking",
        "image":"50.jpg",
        "author":"Hemant",
        "date":date(2022,3,10),
        "title":"Mountain Hiking",
        "excerpt":"Travel alone in mountains make u find yourself yoga karma meditation peace wonder quite beteer naute calm",
        "content":"""
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
        Velit cupiditate voluptatum doloribus atque perferendis vitae, dignissimos earum nostrum. 
        Asperiores veritatis iure error minima incidunt cupiditate exercitationem dolore nobis, reprehenderit deserunt.
        Lorem, ipsum dolor sit amet consectetur adipisicing elit.
         
        Velit cupiditate voluptatum doloribus atque perferendis vitae, dignissimos earum nostrum. 
        Asperiores veritatis iure error minima incidunt cupiditate exercitationem dolore nobis, reprehenderit deserunt.

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
        Velit cupiditate voluptatum doloribus atque perferendis vitae, dignissimos earum nostrum. 
        Asperiores veritatis iure error minima incidunt cupiditate exercitationem dolore nobis, reprehenderit deserunt.
        """
    },
    {
        "slug":"LoveNature",
        "image":"nature.jpg",
        "author":"Sumant",
        "date":date(2022,5,15),
        "title":"Love Nature",
        "excerpt":"Mother nature gives us everyything what we need other we have to protect and save the earth and nature",
        "content":"""
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
        Velit cupiditate voluptatum doloribus atque perferendis vitae, dignissimos earum nostrum. 
        Asperiores veritatis iure error minima incidunt cupiditate exercitationem dolore nobis, reprehenderit deserunt.
        Lorem, ipsum dolor sit amet consectetur adipisicing elit.
         
        Velit cupiditate voluptatum doloribus atque perferendis vitae, dignissimos earum nostrum. 
        Asperiores veritatis iure error minima incidunt cupiditate exercitationem dolore nobis, reprehenderit deserunt.

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
        Velit cupiditate voluptatum doloribus atque perferendis vitae, dignissimos earum nostrum. 
        Asperiores veritatis iure error minima incidunt cupiditate exercitationem dolore nobis, reprehenderit deserunt.
        """
    },
    {
        "slug":"Codingchallenge",
        "image":"code.jpg",
        "author":"Shobhit",
        "date":date(2022,2,1),
        "title":"Coding Challenge",
        "excerpt":"Solve real world probroblems make you better developer and think logical solves the critical problem",
        "content":"""
        Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
        Velit cupiditate voluptatum doloribus atque perferendis vitae, dignissimos earum nostrum. 
        Asperiores veritatis iure error minima incidunt cupiditate exercitationem dolore nobis, reprehenderit deserunt.
        Lorem, ipsum dolor sit amet consectetur adipisicing elit.
         
        Velit cupiditate voluptatum doloribus atque perferendis vitae, dignissimos earum nostrum. 
        Asperiores veritatis iure error minima incidunt cupiditate exercitationem dolore nobis, reprehenderit deserunt.

        Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
        Velit cupiditate voluptatum doloribus atque perferendis vitae, dignissimos earum nostrum. 
        Asperiores veritatis iure error minima incidunt cupiditate exercitationem dolore nobis, reprehenderit deserunt.
        """
    }
]

def get_date(all_posts):
    return all_posts['date']   

def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,"blog/index.html",{"posts":latest_posts})

def post(request):
    sorted_posts=sorted(all_posts,key=get_date)
    arrange_posts=sorted_posts[::-1]
    return render(request,"blog/all-posts.html",{"all_posts":arrange_posts})

def post_detail(request,slug):
    for post in all_posts:
        if post['slug']==slug:
            inventory=post
    return render(request,"blog/post-detail.html",{"post":inventory})