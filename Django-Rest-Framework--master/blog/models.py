from django.db import models

class User(models.Model):

    name = models.CharField(max_length=32)
    email = models.EmailField()

    def __repr__(self):

        return "{}: {}".format(self.pk, self.name)
    __str__ = __repr__

class Entry(models.Model):

    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
        (STATUS_DRAFT,"下書き" ),
        (STATUS_PUBLIC,"公開中")
    )

    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8,choices=STATUS_SET,default=STATUS_DRAFT)
    author = models.ForeignKey(User,related_name="enries",on_delete=models.CASCADE)