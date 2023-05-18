# FSND-capstone
## CASTING AGENCY
This Application will allow to add movies and actors details that can help agency to maintain database and hire actors for different movies.

### APP is hosted at https://udaacity-fsnd-capstone.onrender.com

As this currently contains only backend implementation so we can access endpoints through the postman collection in this repo

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.
### Models:
Movies with attributes title and release date
Actors with attributes name, age and gender
### Endpoints:
- GET /actors and /movies
- GET /actors/<id> and /movies/<id>
- DELETE /actors/<id> and /movies/<id>
- POST /actors and /movies and
- PATCH /actors/<id> and /movies/<id>
  
### Roles:
#### Casting Assistant
      - Can view actors and movies
#### Casting Director
      - All permissions a Casting Assistant has and…
      - Add or delete an actor from the database
      - Modify actors or movies
#### Executive Producer
      - All permissions a Casting Director has and…
      - Add or delete a movie from the database
  
** This project uses Auth0 authentication to get role information through the JWTs created
*** postman collection already has jwts setup for each role but if you want to generate new token you can use following link with provided creds and update them to postmn collection in environment file
  - link- https://capstone-udacity016.us.auth0.com/authorize?audience=identifier-capstone&response_type=token&client_id=Nr1jCzygC1vqPZTqU8fbNXK0OHHiUrqa&redirect_uri=http://localhost:8080
  #### creds for different roles:
  - Casting Assistant username:casting_assistant@abc.com    password:Udacity@123
  - Casting Director username:casting_director@abc.com    password:Udacity@123
  - Executive Producer username:executive_producer@abc.com    password:Udacity@123
