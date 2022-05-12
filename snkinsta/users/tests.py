from django.test import TestCase

#models
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.


class ProfileFollowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='madara',password='suputamdre',email='madara@gmail.com')
        self.user.save()
        self.userb = User.objects.create_user(username='itachi', password='suputamdre1', email='itachi@gmail.com')
        self.userb.save()
        self.profile1 = Profile(user=self.user)
        self.profile1.save()
        self.profile2 = Profile(user=self.userb)
        self.profile2.save()

    def test_profile_created(self):
        qs = Profile.objects.all()
        # print(qs)
        self.assertEqual(qs.count(),2)

    def test_following(self):
        first = self.user
        second = self.userb
        first.profile.followers.add(second) #add a follower
        second_user_following_who = second.following.all()
        qs = second_user_following_who.filter(user=first)#from a user ,check other user is being followed
        # print(qs)
        # qs = second.followers_set.filter(user=user_a) its the same
        first_user_following_no_one = first.following.all()#check new user hasnt following anyone
        self.assertTrue(qs.exists())
        self.assertFalse(first_user_following_no_one.exists())

    # p = Profile.objects.first() -> get de user profile
    # p.followers.add(someUser) -> add a follower for a user
    # p.followers.all() -> all users following this profile/user

    # user.following.all() -> all users i follow.
    # user has acces to the list of user in profile model followers

    # user.followers_set.all -> is the same without related name

    # followers add or remove a user from a user profile
    # following show how many users the user follow