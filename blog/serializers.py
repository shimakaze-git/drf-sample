from rest_framework import serializers
from .models import Member, Article


class MemberSerializer(serializers.ModelSerializer):
    """MemberのSerializer."""

    birthday = serializers.DateField(
        input_formats=['%Y-%m-%d', '%Y/%m/%d'],
        format='%Y年%m月%d日'
    )

    class Meta:
        modle = Member
        # db_table = ''
        managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
        fields = ('id', 'name', 'email', 'birthday')


class ArticleSerializer(serializers.ModelSerializer):
    """ArticleのSerializer."""

    member_id = serializers.IntegerField(write_only=True)
    member = MemberSerializer(read_only=True)

    status_name = serializers.SerializerMethodField()

    class Meta:
        modle = Article
        # db_table = ''
        managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
        fields = (
            'title',
            'content',
            'status',
            'member_id',
            'member',
            'status_name'
        )

    def get_status_name(self, obj):
        """statusの項目を返す."""
        return obj.get_status_display()
