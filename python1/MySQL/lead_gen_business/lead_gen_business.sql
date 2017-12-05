-- 1. What query would you run to get the total revenue for March of 2012?
SELECT MONTHNAME(charged_datetime) AS month, SUM(amount) AS amount
FROM billing
WHERE MONTHNAME(charged_datetime) = 'March' AND YEAR(charged_datetime) = 2012
GROUP BY MONTHNAME(charged_datetime);

-- 2. What query would you run to get total revenue collected from the client with an 
-- id of 2?
SELECT clients.client_id AS id, SUM(billing.amount) AS amount
FROM clients
	JOIN billing ON clients.client_id = billing.client_id
WHERE clients.client_id = 2;

-- 3. What query would you run to get all the sites that client=10 owns?
SELECT clients.client_id AS id, sites.domain_name AS domain_name
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
WHERE clients.client_id = 10;

-- 4. What query would you run to get total # of sites created per month per year for 
-- the client with an id of 1? What about for client=20?
SELECT clients.client_id AS id, COUNT(sites.domain_name) AS number_of_websites, 
MONTHNAME(charged_datetime) AS month_created, YEAR(charged_datetime) AS year_created
FROM sites
	JOIN clients ON sites.client_id = clients.client_id
    JOIN billing ON clients.client_id = billing.client_id
WHERE clients.client_id = 1 -- sub 20 for second question
GROUP BY MONTHNAME(charged_datetime), YEAR(charged_datetime)
ORDER BY YEAR(charged_datetime);

-- 5. What query would you run to get the total # of leads generated for each of the sites 
-- between January 1, 2011 to February 15, 2011?
SELECT sites.domain_name AS website , COUNT(leads.leads_id) AS leads, 
DATE_FORMAT(leads.registered_datetime, "%M %d %Y") AS date_generated
FROM leads
	JOIN sites ON leads.site_id = sites.site_id
WHERE leads.registered_datetime
BETWEEN STR_TO_DATE('2011-01-01','%Y-%m-%d') AND STR_TO_DATE('2011-02-15','%Y-%m-%d')
GROUP BY DATE_FORMAT(leads.registered_datetime, "%M %d %Y"), sites.domain_name
ORDER BY DATE_FORMAT(leads.registered_datetime, "%M %d %Y") DESC;

-- 6. What query would you run to get a list of client names and the total # of leads 
-- we've generated for each of our clients between January 1, 2011 to December 31, 2011?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, 
COUNT(leads.leads_id) AS leads
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    JOIN leads ON sites.site_id = leads.site_id
GROUP BY CONCAT(clients.first_name, ' ', clients.last_name);

-- 7. What query would you run to get a list of client names and the total # of leads 
-- we've generated for each client each month between months 1 - 6 of Year 2011?
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name,
COUNT(leads.leads_id) AS leads, MONTHNAME(leads.registered_datetime) AS month
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime
BETWEEN STR_TO_DATE('2011-01-01','%Y-%m-%d') AND STR_TO_DATE('2011-06-30', '%Y-%m-%d')
GROUP BY CONCAT(clients.first_name, ' ', clients.last_name),
MONTHNAME(leads.registered_datetime);

-- 8. What query would you run to get a list of client names and the total # of leads 
-- we've generated for each of our clients' sites between January 1, 2011 to December 
-- 31, 2011? Order this query by client id.
SELECT clients.client_id, CONCAT(clients.first_name, ' ', clients.last_name) AS name,
COUNT(leads.leads_id) AS leads
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime
BETWEEN STR_TO_DATE('2011-01-01','%Y-%m-%d') AND STR_TO_DATE('2011-12-31', '%Y-%m-%d')
GROUP BY clients.client_id;

-- Come up with a second query that shows all the clients, the site name(s), and the 
-- total number of leads generated from each site for all time.
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, sites.domain_name,
COUNT(leads.leads_id) AS leads
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
    JOIN leads ON sites.site_id = leads.site_id
GROUP BY CONCAT(clients.first_name, ' ', clients.last_name), sites.domain_name;

-- 9. Write a single query that retrieves total revenue collected from each client for 
-- each month of the year. Order it by client id.
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, 
SUM(billing.amount) AS revenue, DATE_FORMAT(billing.charged_datetime, '%M') AS month, 
DATE_FORMAT(billing.charged_datetime, '%Y') AS year
FROM clients
	JOIN billing ON clients.client_id = billing.client_id
GROUP BY CONCAT(clients.first_name, ' ', clients.last_name),
DATE_FORMAT(billing.charged_datetime, '%M'), DATE_FORMAT(billing.charged_datetime, '%Y');

-- 10. Write a single query that retrieves all the sites that each client owns. Group the 
-- results so that each row shows a new client. It will become clearer when you add a new 
-- field called 'sites' that has all the sites that the client owns. 
-- (HINT: use GROUP_CONCAT)
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS name, 
GROUP_CONCAT(sites.domain_name) as sites
FROM clients
	JOIN sites ON clients.client_id = sites.client_id
GROUP BY CONCAT(clients.first_name, ' ', clients.last_name);