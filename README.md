# Movie-Ticket-Booking-System
Django REST API for Movie Ticket Booking — AlignTurtle Internship Assignment by Panchagiri Raju
Project Name : Movie Ticket Booking System

 Project Description :
The Movie Ticket Booking System is designed to provide a seamless backend experience for users wishing to book movie tickets. This project utilizes Python and Django alongside the Django REST Framework to ensure a robust and scalable solution. The backend supports user authentication, movie management, show scheduling, seat booking, and booking management through a secure API interface. 

Key features include user signup and login with JWT authentication, browsing available movies and showtimes, booking and managing seats, and comprehensive API documentation via Swagger. The system enforces business rules to maintain data integrity and prevent booking conflicts.

 Key Milestones Achieved

1. *User Authentication*: 
   - Implemented user signup and login functionality secured by JWT tokens.
   - Developed token generation and validation processes.

2. *Django Models Design*:
   - Created Django models for Movie, Show, and Booking.
   - Established relationships and constraints to maintain referential integrity.
   - Example Model Relationships:
     - A Movie can have multiple Shows.
     - A Show can have multiple Bookings.
     - Each Booking is linked to a specific User and Show.

3. *API Endpoint Development*:
   - Developed RESTful API endpoints for:
     - Listing Movies (GET /movies)
     - Viewing Shows for a specific Movie (GET /movies/{id}/shows)
     - Booking Seats (POST /bookings)
     - Canceling Bookings (DELETE /bookings/{id})
     - Listing User Bookings (GET /users/{id}/bookings)
   - Ensured secure access via JWT authentication methods.

4. *Swagger Documentation Integration*:
   - Integrated Swagger for API documentation.
   - Created detailed request/response schemas for each endpoint.
   - Added guidelines for JWT authentication in the documentation.

5. *Business Rule Enforcement*:
   - Implemented logic to prevent double bookings and overbooking.
   - Established processes to free up seats upon cancellation.
   - Enabled transaction rollback in case of booking failures.

6. *Comprehensive Documentation*:
   - Prepared an extensive README file containing:
     - Setup instructions
     - Usage guidelines
     - API endpoint descriptions
     - Authentication process

 Bonus Tasks Completed:
- Implemented retry logic for concurrent booking requests to ensure data integrity.
- Developed robust error handling mechanisms to provide meaningful feedback on API failures.
- Included input validations to maintain the integrity and cleanliness of user inputs.
- Conducted security checks to protect against common vulnerabilities.

 Project Outcome :
The Movie Ticket Booking System successfully delivers a functional backend capable of handling user interactions with movies and bookings efficiently. The use of JWT for authentication ensures a secure environment for user data. The RESTful API is well-structured and documented through Swagger, making it accessible for developers and testers.
The system maintains critical business logic to prevent data conflicts, ensuring a reliable booking experience for users. Furthermore, the project demonstrates best practices in backend development through clean and modular code, comprehensive documentation, and adherence to security standards.

 Conclusion :
The Movie Ticket Booking System project showcases the ability to design and implement a complete backend solution for a real-world application. The end product meets the original objectives of providing a secure and efficient movie booking experience, highlighting proficiency in Python, Django, and RESTful API design. Future enhancements may include frontend integration, user feedback systems, and advanced booking analytics.
