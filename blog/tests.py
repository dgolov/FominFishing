from django.test import TestCase

from .models import Category, Post


class TestCategoryModel(TestCase):
    """ Tests for category model
    """
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test')

    def test_name_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_name_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEquals(max_length, 150)

    def test_name_max_blank(self):
        category = Category.objects.get(id=1)
        blank = category._meta.get_field('name').blank
        self.assertEquals(blank, False)

    def test_name_max_null(self):
        category = Category.objects.get(id=1)
        null = category._meta.get_field('name').null
        self.assertEquals(null, False)

    def test_object_name_is_name(self):
        category = Category.objects.get(id=1)
        expected_object_name = category.name
        self.assertEquals(expected_object_name, str(category))


class TestPostModel(TestCase):
    """ Test for post model
    """
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(name='Test')
        Post.objects.create(category=category, title='Test', text='Hello World', poster=None, slug='test')

    def test_category_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'Категория')

    def test_category_blank(self):
        post = Post.objects.get(id=1)
        blank = post._meta.get_field('category').blank
        self.assertEquals(blank, False)

    def test_category_null(self):
        post = Post.objects.get(id=1)
        null = post._meta.get_field('category').null
        self.assertEquals(null, False)

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Заголовок')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 150)

    def test_title_blank(self):
        post = Post.objects.get(id=1)
        blank = post._meta.get_field('title').blank
        self.assertEquals(blank, False)

    def test_title_null(self):
        post = Post.objects.get(id=1)
        null = post._meta.get_field('title').null
        self.assertEquals(null, False)

    def test_text_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'Текст поста')

    def test_text_blank(self):
        post = Post.objects.get(id=1)
        blank = post._meta.get_field('text').blank
        self.assertEquals(blank, False)

    def test_text_null(self):
        post = Post.objects.get(id=1)
        null = post._meta.get_field('text').null
        self.assertEquals(null, False)

    def test_poster_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('poster').verbose_name
        self.assertEquals(field_label, 'Обложка')

    def test_poster_blank(self):
        post = Post.objects.get(id=1)
        blank = post._meta.get_field('poster').blank
        self.assertEquals(blank, True)

    def test_poster_null(self):
        post = Post.objects.get(id=1)
        null = post._meta.get_field('poster').null
        self.assertEquals(null, True)

    def test_created_at_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('created_at').verbose_name
        self.assertEquals(field_label, 'Создано')

    def test_created_at_auto_now_add(self):
        post = Post.objects.get(id=1)
        auto_now_add = post._meta.get_field('created_at').auto_now_add
        self.assertEquals(auto_now_add, True)

    def test_created_at_auto_now(self):
        post = Post.objects.get(id=1)
        auto_now = post._meta.get_field('created_at').auto_now
        self.assertEquals(auto_now, False)

    def test_created_at_blank(self):
        post = Post.objects.get(id=1)
        blank = post._meta.get_field('created_at').blank
        self.assertEquals(blank, True)

    def test_created_at_null(self):
        post = Post.objects.get(id=1)
        null = post._meta.get_field('created_at').null
        self.assertEquals(null, False)

    def test_updated_at_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('updated_at').verbose_name
        self.assertEquals(field_label, 'Обновлено')

    def test_updated_at_auto_now_add(self):
        post = Post.objects.get(id=1)
        auto_now_add = post._meta.get_field('updated_at').auto_now_add
        self.assertEquals(auto_now_add, False)

    def test_updated_at_auto_now(self):
        post = Post.objects.get(id=1)
        auto_now = post._meta.get_field('updated_at').auto_now
        self.assertEquals(auto_now, True)

    def test_updated_at_blank(self):
        post = Post.objects.get(id=1)
        blank = post._meta.get_field('updated_at').blank
        self.assertEquals(blank, True)

    def test_updated_at_null(self):
        post = Post.objects.get(id=1)
        null = post._meta.get_field('updated_at').null
        self.assertEquals(null, False)

    def test_photos_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('photos').verbose_name
        self.assertEquals(field_label, 'Фотографии')

    def test_photos_blank(self):
        post = Post.objects.get(id=1)
        blank = post._meta.get_field('photos').blank
        self.assertEquals(blank, True)

    def test_photos_null(self):
        post = Post.objects.get(id=1)
        null = post._meta.get_field('photos').null
        self.assertEquals(null, False)

    def test_slug_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'Ссылка')

    def test_slug_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('slug').max_length
        self.assertEquals(max_length, 150)

    def test_slug_blank(self):
        post = Post.objects.get(id=1)
        blank = post._meta.get_field('slug').blank
        self.assertEquals(blank, False)

    def test_slug_null(self):
        post = Post.objects.get(id=1)
        null = post._meta.get_field('slug').null
        self.assertEquals(null, False)

    def test_object_name_is_title(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEquals(expected_object_name, str(post))
