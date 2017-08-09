#!/usr/bin/python 2.7


import psycopg2


DBNAME = "news"


def most_popular_articles():
    """Returns most popular articles"""
    return_string = " "
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select articles.title, count(*) as view_count
        from articles join log on log.path like '%'||articles.slug||'%'
        where log.status != '404 NOT FOUND'
        group by articles.title
        order by view_count desc limit 3;
        """)
    answer = c.fetchall()
    print "The three most popular articles are: \n"
    for x in answer:
    	print "      Article Name: ", x[0], " --- ",  x[1], " views"
    db.close()
    return return_string


def most_popular_authors():
    """Returns most popular authors"""
    return_string = " "
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select authors.name, count(*) as view_count
        from articles join log on log.path like '%'||articles.slug||'%'
        left join authors on authors.id = articles.author
        where log.status != '404 NOT FOUND'
        group by authors.name
        order by view_count desc;
                """)
    answer = c.fetchall()
    print "The authors in order of their popularity are: \n"
    for x in answer:
        print "      Author Name: ", x[0], " --- ",  x[1], " views"
    db.close()
    return return_string


def most_errors():
    """Returns the days where the errors were greater than 1%"""
    return_string = " "
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""
        select time::timestamp::date, error_count / total_count::float
        from(
            select time::timestamp::date, count(*) as total_count,
            sum(case when log.status = '404 NOT FOUND' then 1 else 0 end)
            error_count
            from log
            group by log.time::timestamp::date
            order by total_count desc)
        as new_table
        where error_count / total_count::float >= 0.01;
                """)
    answer = c.fetchall()
    print "The date(s) on which the errors were greater than 1 percent: \n"
    for x in answer:
        print "      Date: ", x[0], " --- ",  x[1] * 100, " percent errors!"
    db.close()
    return return_string


print most_popular_articles()
print most_popular_authors()
print most_errors()
