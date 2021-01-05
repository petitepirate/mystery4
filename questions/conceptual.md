## Conceptual Exercise

### Answer the following questions below:

**1. What is PostgreSQL?**  
A highly stable open source object relational database management system, first released in 1996

**2. What is the difference between SQL and PostgreSQL?**  
PostgreSQL is an advanced version of SQL providing support to different functions of SQL like foreign  
keys, subqueries, triggers, and different user-defined types and functions. In general PostgreSQL is  
known for having additional robust features over SQL.

**3. In `psql`, how do you connect to a database?**  
psql db_name or \c db_name

**4. What is the difference between `HAVING` and `WHERE`?**  
WHERE is used to filter records before any groupings take place. HAVING is used to filter values after  
they have been groups. Only columns or expressions in the group can be included in the HAVING clause's  
conditions

**5. What is the difference between an `INNER` and `OUTER` join?**  
The major difference between INNER and OUTER joins is that INNER joins result in the intersection of  
two tables, whereas OUTER joins result in the union of two tables.  In other words - INNER join returns  
only the rows that match a given condition in both tables whereas OUTER joins returns all rows of the  
two tables.

**6. What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?**  
LEFT OUTER returns all rows from the FROM clause (aka first table) and rows from the second table that  
match the queried condition. RIGHT OUTER does the inverse where it returns all rows from the JOIN clause  
(aka second table) and rows from the first table that match the queried condition.

**7. What is an ORM? What do they do?**  
ORM stands for object-relational mapper.  An ORM s a code library that automates the transfer of data  
stored in relational database tables into objects that are more commonly used in application code.  
Basically it allows you to manipulate data not by writing SQL, but by interacting directly with an object  
in the same language you're using - which for us is python. PostgreSQL is an ORM.

**8. What are some differences between making HTTP requests using AJAX and from the server side using**  
**a library like `requests`?**  
The main behavioral difference is on the client side.  When the browser makes a regular request as  
in window.location.href = "index.html", it clears the current window and loads the server response  
into the window. With an ajax request, the current window/document is unaffected and javascript code  
can examine the results of the request and do what it wants to with those results (insert HTML  
dynamically into the page, parse JSON and use it the page logic, parse XML, etc...). The server doesn't  
do anything different - it's just in how the client treats the response from the two requests. Also server  
side libraries and requests keeps information like API keys, passwords and other sensitive data from  
being exposed to the browser and end-user.

**9. What is CSRF? What is the purpose of the CSRF token?**  
CSRF stands for cross-site request forgery. CSRF tokens can prevent CSRF attacks by making it impossible  
for an attacker to construct a fully valid HTTP request suitable for feeding to a victim user.  Basically  
a CSRF token is associated with a particular user and can be found as a hidden value in every state  
changing form which is present on the web application.  The token prevents people from hijacking simple  
HTTP requests by requiring the specific token.

**10. What is the purpose of `form.hidden_tag()`?**  
The form.hidden_tag() template argument generates one or several hidden fields in Flask-WTF that includes  
a token that is used to protect the form against CSRF attacks. All you need to do to have the form protected  
is include this hidden field and have the SECRET_KEY variable defined in the Flask configuration.
