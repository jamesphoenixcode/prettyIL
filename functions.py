import instaloader
import os

L = instaloader.Instaloader()
L.load_session_from_file("username")

rootWorkingDirectory = os.getcwd() 

def comparator2000(targetUsername: str) -> str:
    '''
    This function check if the ```targetUsername`` folder exists, if not, create one and enter.
    '''
    # Check if exists, if not, create.
    if not os.path.exists(targetUsername):
        os.makedirs(targetUsername)
    
    # Changue directory to targetUsername
    os.chdir(targetUsername)
    return str(f"Im here {os.getcwd()}, tick.")
    

def comparator3000(targetUsername: str, downloadType: str) -> str:
    '''
    This function will test if the directory of the ``targetUsername`` exists, if not create the folder
    and enter, the same for ``downloadType`` which is the name of the media type being downloaded,
    currently are: ``Posts``, ``Stories``, ``Highlights``.
    '''

    # Check if dir exists, if not, create.
    if not os.path.exists(targetUsername):
        os.makedirs(targetUsername)

    # Changue dir to the target username's
    os.chdir(targetUsername)

    # Check if exists the highlights folder if not, create
    if not os.path.exists(downloadType):
        os.makedirs(downloadType)

    # Changue working dir to the highlight folder
    os.chdir(downloadType)
    return str(f"Im here {os.getcwd()}, tick.")


def downloadHL(Lcontext, targetUsername: str, rootWD):

    comparator3000(targetUsername, "Highlights")

    # Get the list of the aviable highlights os the target and download,
    # every folder, has his original title. 
    for highlight in L.get_highlights(instaloader.Profile.from_username(Lcontext, targetUsername)):
        print(highlight.cover_url + '\nCurrently its not possible to download original highlight cover due to InstaLoader Lib.')
        for item in highlight.get_items():
            L.download_storyitem(item, highlight.title)

    # Changue the working dir to the given in the function,
    # i recommend to put every profile in a single folder "root working dir"
    os.chdir(rootWD)
    return 0

def downloadStories(Lcontext, targetUsername: str, rootWD):

    comparator3000(targetUsername, "Stories")

    userData = instaloader.Profile.from_username(Lcontext, targetUsername)

    for story in L.get_stories([userData.userid]):
        for item in story.get_items():
            L.download_storyitem(item, f"{str(item.date).replace(' ', '_', 1).replace(':', '-').replace(' ', '')}_UTC")
    
    os.chdir(rootWD)
    return 0

def downloadPosts(Lcontext, targetUsername: str, rootWD):

    comparator3000(targetUsername, "Posts")

    userData = instaloader.Profile.from_username(Lcontext, targetUsername)

    posts = userData.get_posts()

    print(f'Profile: {userData.username}, contain: {posts.count} posts.')

    for post in posts:
        L.download_post(post, post.date_utc)
        L.download_comments = True
        L.download_geotags = True

    os.chdir(rootWD)
    return 0

def downloadProfilePic(Lcontext, targetUsername: str, rootWD):

    userData = instaloader.Profile.from_username(Lcontext, targetUsername)

    comparator3000(targetUsername, "Profile Pictures")

    

    os.chdir(rootWD)
    return 0

def writeUserMD(Lcontext, targetUsername: str, rootWD):
    comparator2000(targetUsername)
    profileData = instaloader.Profile.from_username(Lcontext, targetUsername)
    # This will download only the user profile to a pretty json file. 
    instaloader.save_structure_to_file(profileData, f"{targetUsername}.json")
    # This will write the resume of the profile in a text file.
    with open(f"{targetUsername}_resume.txt", "w", encoding="utf-8") as f:
        f.writelines(f"{profileData.full_name}\nTotal posts: {profileData.mediacount}\nTotal Followers: {profileData.followers}\nFollowing: {profileData.followees}\n{profileData.biography}\n{profileData.external_url}\nSponsors:\n{profileData.entities}")
    os.chdir(rootWD)
    return 0

# downloadPosts(L.context, username, rootWorkingDirectory)
# profileJSON = "n"
# dumpedJSON = json.dumps(profileJSON, sort_keys=True, indent=4, ensure_ascii=False)
# print(dumpedJSON)


# def downloadIGTV(Lcontext, targetUsername: str, rootWD):

#     comparator3000(targetUsername, "IGTV")

#     userData = instaloader.Profile.from_username(Lcontext, targetUsername)
#     igtvPosts = userData.get_igtv_posts()

#     for post in igtvPosts:
#         print(post.title)  
