#!/usr/bin/python
import praw
import time
import post

# Initialize our bot
user_agent = ("Analytics Bot 0.1")
r = praw.Reddit(user_agent = user_agent)

# Select a subreddit
subreddit = r.get_subreddit("askreddit")

# Initialize array for tracked posts
tracked_posts = []

# Begin main execution loop
while True:

    # Grab any new posts
    print "\n ---------------------------------- \n Checking for new posts \n"
    for submission in subreddit.get_new(limit = 10):

        # Create a new post object
        new_post = post.Post(submission.title, submission.id)

        if new_post not in tracked_posts:
            tracked_posts.append(new_post)
            print "New Post: ", new_post.title

    # Track score changes for 5 minutes
    minutes = 5
    while minutes > 0:
        print "\n\n Updating tracked posts"

        for current_post in tracked_posts:
            submission = r.get_submission(submission_id = current_post.id)
            current_post.addScore(submission.score)
            #slope = current_post.calculateChange()
            print "\nAverage slope for post ", current_post.title, "is ", current_post.calculateChange()

        print "\n Minutes remaining = ", minutes
        minutes = minutes - 1

        time.sleep(60)