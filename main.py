import django_setup
from post_system.models import Author, Post, Comment

def main():
    while True:
        q = input('''Що ви хочете зробити? \n
                1-Додати нового автора\n
                2-Створити пост\n
                3-Додати коментар до посту\n
                4-Відредагувати текст посту\n
                5-Переглянути коментарі до посту\n 
                6-Переглянути всі пости та їх айді\n
                7-Quit\n''')

        match q:
            case "1":
                first_name = input("Введіть ім'я автора: ")
                last_name = input("Введіть прізвище автора: ")
                bio = input("Введіть опис автора: ")
                Author(
                    first_name = first_name,
                    last_name = last_name,
                    bio = bio
                ).save()
                print("Авторa додано!")
            case "2":
                name = input("Введіть назву поста: ")
                content = input("Введіть текст поста: ")
                author_id = input("Введіть айді автора: ")
                author = Author.objects.get(id = author_id)
                Post(
                    name = name,
                    content = content,
                    author = author
                ).save()
            case "3":
                post = input("Введіть айді поста: ")
                text = input("Введіть текст коментаря: ")
                author = input("Введіть айді автора: ")
                author = Author.objects.get(id = author)
                post = Post.objects.get(id = post)
                Comment(
                    text = text,
                    post = post,
                    author = author
                ).save()
            case "4":
                post = input("Введіть айді поста: ")
                content = input("Введіть новий контент: ")
                Comment.objects.filter(id = post).update(content = content)
            case "5":
                post = input("Введіть айді поста: ")
                post = Post.objects.get(id = post)
                comments = Comment.objects.filter(post = post)
                for comment in comments:
                    print(comment)
            case "6":
                posts = Post.objects.all()
                print("Список постів:")
                for post in posts:
                    print(post,f'\nКонтент:{post.content}', f'\nid:{post.id}')
            case "7":
                break

if __name__ == "__main__":
    main()



