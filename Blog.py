import sqlite3

def create_database():
    connect = sqlite3.connect('blog.db')
    cursor = connect.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        creator TEXT NOT NULL
    )
    ''')
    connect.commit()
    connect.close()

def add_post(title, creator):
    connect = sqlite3.connect('blog.db')
    cursor = connect.cursor()
    cursor.execute(''' INSERT INTO posts (title, creator) VALUES (?, ?)''', (title, creator))
    connect.commit()
    connect.close()
    return "Post added successfully"

def get_all_posts():
    connect = sqlite3.connect('blog.db')
    cursor = connect.cursor()
    cursor.execute(''' SELECT * FROM posts ''')
    posts = cursor.fetchall()
    connect.close()
    return posts

def remove_post(post_id):
    connect = sqlite3.connect('blog.db')
    cursor = connect.cursor()
    cursor.execute(''' DELETE FROM posts WHERE id = ? ''', (post_id,))
    connect.commit()
    connect.close()
    return "Post removed successfully"

def input_post_details():
    title = input("Enter the post title: ")
    creator = input("Enter the creator's name: ")
    return title, creator

def update_post(post_id, new_title, new_creator):
    connect = sqlite3.connect('blog.db')
    cursor = connect.cursor()
    cursor.execute(''' UPDATE posts SET title = ?, creator = ? WHERE id = ? ''', (new_title, new_creator, post_id))
    connect.commit()
    connect.close()
    return "Post updated successfully"

def main():
    create_database()
    while True:
        print("1. Add Post")
        print("2. View All Posts")
        print("3. Remove Post")
        print("4. Update Post")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            title, creator = input_post_details()
            message = add_post(title, creator)
            print(message)
        elif choice == '2':
            posts = get_all_posts()
            for post in posts:
                print(f"ID: {post[0]}, Title: {post[1]}, Creator: {post[2]}")
        elif choice == '3':
            post_id = int(input("Enter the post ID to remove: "))
            message = remove_post(post_id)
            print(message)
        elif choice == '4':
            post_id = int(input("Enter the post ID to update: "))
            new_title, new_creator = input_post_details()
            message = update_post(post_id, new_title, new_creator)
            print(message)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()