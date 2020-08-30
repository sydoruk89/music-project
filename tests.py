from music.models import Music
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class MusicTests(TestCase): 

    def setUp(self): 
        self.user = get_user_model().objects.create_user(
            username = "test", 
            password = "pass"
        )

        self.music = Music.objects.create(
            title='Test Album', 
            author="queen", 
            genre='pop',
            artist=self.user, 
            body="Test Description", 
            time='2am 8-29-2020'
        )
        
        self.music.save()
        self.record = Music.objects.get(pk=1)

    def test_model_content(self): 
        self.assertEqual(self.record, self.music)

    def test_model_name(self): 
        self.assertEqual(self.record.title, self.music.title)

    def test_create_redirect_home(self): 
        response = self.client.post(reverse("create"),{
            "title" : "Test Album", 
            "author" : "queen",
            "genre": "pop",
            "artist" : self.user, 
            "body" : "Test Description",
            "time": "2am 8-29-2020",
        } 
        , follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed("home.html")