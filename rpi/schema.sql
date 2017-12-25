drop table if exists notifications;
create table notifications (
    id integer primary key autoincrement,
    date datetime not null,
    topic text not null,
    payload text not null
);