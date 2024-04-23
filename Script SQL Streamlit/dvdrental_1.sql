'''select fa.actor_id, concat(a.first_name, ' ',a.last_name) as full_name, fa.film_id, f.title, f.release_year, l.name as "language" from film_actor fa
join actor a
on a.actor_id = fa.actor_id
join film f
on fa.film_id = f.film_id
join language l
on f.language_id = l.language_id '''

'''select rating, count(title) from film
group by rating'''

select f.title, c.name from film f
join film_category fc
on f.film_id = fc.film_id 
join category c
on c.category_id = fc.category_id