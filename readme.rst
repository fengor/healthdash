HealthDash
==========

This project is for the vizualization of some personal health data I collect. It is part of my suite of QuantifiedSelf Helpers. It has the following modules

Bodyweight
----------

Tracked variables are total bodyweight in kg and bodyfat percentage. Calculated from that is the lean body mass.


* GET    http://localhost:8000/weight/ - lists all weight entries
* GET    http://localhost:8000/weight/YYYY-MM-DD - shows the weight entry for the specified date
* POST   http://localhost:8000/weight/ - creates a new weight entry
* PUT    http://localhost:8000/weight/YYYY-MM-DD - updates the weight entry for the specified date
* DELETE http://localhost:8000/weight/YYYY-MM-DD - deletes the weight entry for the specified date

not yet implemented:

* GET    http://localhost:8000/weight/new - shows the weight entry form


