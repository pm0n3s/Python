-- used to insert into users
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Chris', 'Baker', NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Diana', 'Smith', NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('James', 'Johnson', NOW(), NOW());
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES ('Jessica', 'Davidson', NOW(), NOW());

-- used to insert into friendships
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 2, NOW(), NOW());
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 3, NOW(), NOW());
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (1, 4, NOW(), NOW());
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (2, 1, NOW(), NOW());
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (3, 1, NOW(), NOW());
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (4, 1, NOW(), NOW());

-- used to display data as shown in example
SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, 
user2.last_name AS friend_last_names 
FROM users
	LEFT JOIN friendships ON users.id = user_id
	LEFT JOIN users AS user2 ON user2.id = friend_id
ORDER BY users.id;