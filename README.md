# Take Stock

![4 size view of the website's home page]()

<!-- Description -->
Take Stock is a data handling app for small buisnesses to take care of their stock and product information. A company can create a profile, add stock items, add products, and then link stock items to each product. The app will then tell the user exactly how many of each product they can make based on what they have in stock. 

## User Experience (UX)

### User Stories / Epics 

- Epic
  - As a user/company, I'd like to have an app where I can store information about my products; including its:
    - Name
    - List of parts (Bill of Materials (BOM))
    - How many of each item I have in stock
    - How many of each product I can make
  - I would like to be able to update the products BOM at any time, as well as the stock list.
  - Login/logout should be quick and easy.
         
- First time visitor goals:
  - Have the first visit easily explain the site, how it works, what it can do, etc.
  - Have the app be easy to navigate and intuitive to use.
  - Be able to sign up for an account as easily as possible.

- Returning visitor goals:
  - Be able to login and see data stored from previous visits.
  - Be able to easily login and view my data.

- Frequent user goals:
  - Be able to quickly see what I have in stock and how many products I can make.
  - Be able to add new products and/or stock quickly and easily and see that
    immediately reflected in the interface.

- Admin user goals:
  - Have access to other user data to be able to check for and remove objectionable inputs.

- Site owner goals: 
  - Have the interface be easy to navigate and reflect recent actions to the user. 
  - Show the user exactly how many of each product they can make.
  - Have user data be only accessable to that specific user.

- User acceptance: 
  - Stock list and product list implemented.
  - Register/login feature to separate user data.
  - User data cannot be accessed or change by the wrong user.

- Tasks:
  - Implement login/logout features.
  - Create models to house stock and product data.
  - Create logic to link stock items to products.
  - Allow users to update and delete their data as they choose to.
  - Allow the admin access to all user data.

### Design
- Color Scheme
  - Sleek, black on white with sophisticated color scheme accents to portray professionalism.

- Typography
  - Nanum Gothic is and easy to read, block-like typeface. The motif of the app is professional which the font follows.

- Imagery
  - No imagery as the app is informational based. Screenshots on the home page and the "how-to-use" page to show functionality and use.

- Wireframes 

  - Wireframes were constructed in a whiteboard as the design motif was minimal. Simple lines and boxes were used throughout.
  
- Home page

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/wireframes/home.jpg" style="max-height: 300px;">

- Logged in home page

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/wireframes/logged_in_home.jpg" style="max-height: 300px;">

- Lists

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/wireframes/stock.jpg" style="max-height: 300px;">

- Product page

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/wireframes/products.jpg" style="max-height: 300px;">

- Forms

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/wireframes/form.jpg" style="max-height: 300px;">

- Admin

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/wireframes/admin.jpg" style="max-height: 300px;">


<!-- HTML used instead of markdown to control image size as images were very large when testing. -->

## Features

### Existing features
- Users can add stock and products, as well as link stock items to products.
- The app will show users exactly how many of each product the user can make given the amount of stock they have.
- The app has all features of CRUD functionality.

### Landing page

- There are two versions of the landing page: logged in and logged out. The logged out landing page gives brief information about the app and a help guide as to how the app works. The logged in landing page allows a user user access to their stock list and product list. From these pages they can manipulate their data however they choose to.

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/images/home_page_1.PNG" style="max-height: 300px;">

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/images/home_page_2.PNG" style="max-height: 300px;">


### Stock page 

- A list of all a user's stock with links to update each item or add a new one that redirect to easy to follow forms. 

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/images/README_stock_page.PNG" style="max-height: 300px;">

### Products page 

- A list of all a user's products with a count as to how many of each product can be made based on the number of each linked stock item in the stock list. Each product can be navigated into which will display a list of all it's parts. New parts can be added, or parts can be removed, or the whole product can be deleted from here.

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/images/README_product_page.PNG" style="max-height: 300px;">

### Admin View 

- The Admin View lists all users, all their respective stock and products, and all those product's respective parts. The admin from here can delete any item if it is deemed to be objectionable. 

<img src="/workspace/stock_take_app/stock_take/stock/static/assets/images/admin_view.PNG">

## Future updates

- An orders page where users can specify how many of each product they need to make, and the app with tell them how many they can make, and how much stock they would need to aquire to complete each order.

- Roles relevant to different departments. For example:
  - Managers: Full access to all features
  - Sales: Able to add, update, and change orders
  - Storage: Able to change stock numbers and items
  - Production Hands: Able to read data but not able to change or update data.

- Search bars on Stock and Products pages, as well as when linking parts to products for ease of use. Users will be able to fast-track their experience through the site.

## Languages Used

- HTML5
- CSS3
- JavaScript
- Python and Django

## Frameworks used

- [Google Fonts](https://fonts.google.com/)
- Git
- GitHub
- jQuery

## Agile development

- The project was constructed using Agile methodology, as can be seen in the GitHub repository's Projects section. 

## Testing

- A total of 18 automated tests were ran in Django's Unittest. Tests were conducted on URLs, views, and forms. 
  - For URLs, the automated tests ensured that each page resolved to the correct location. URLs that required arguments to resolve where tested manually using multiple users to ensure they could only access pages with their data on it.

  - For views, automated tests tested for GET requests only. POST request were tested manually.

  - For forms, automated tests were performed for valid and invalid forms. Login and register forms were tested manually:
    - Logging in and register forms show errors if applicable.

- Manual testing of the site was undertaken at every step of development. 

- All URLs were followed to ensure they resolved correctly. An error message page is displayed to a user who tries to navigate to a page they shuoldn't have access to and allows them to navigate back to the home page.

- All CRUD functionality on the user end was tested manually. Products, Stock items, and Product/Part links all work as expected and users only have access to their own data when guided through forms.

- Forms have validation and will not post data if any errors are raised.

- The original project was constructed on a laptop with a screen size of 12.3 inches. The code was put through validators and passed through without any issues.

  - [W3C Markup Validator]()

  - [W3C CSS Validator]()

  - Javascript Validator - JShint
  <!-- Images here -->

  - The JavaScript code was passed with /* jshint esversion: 6 */ above it which removed warnings for setting variables with 'let'.

### Known bugs

## Further testing
- The site was tested on Google Chrome using their developer tools and viewed on Firefox, Microsoft Edge, and Safari to ensure it worked across multiple platforms. The site was also viewed on multiple devices of varying screen sizes.
<!-- Say more  -->

- Google Chrome's DevTools Lighthouse:
  - Desktop
        ![Lighthouse score for desktop]()
  - Mobile
        ![Lighthouse score for mobile]()

## Deployment 
<!-- Heroku deployment here -->
<!-- Deployment code and content taken straight from Code Institutes README template -->

- You can view the live site [here]().

## Credits 

### Code

- Code
  - All code was written by the developer.

### Content

- Content
  - All content was written by the developer.

### Acknowledgements
    
- Tutor support at Code Institute for all their support throughout.

- Friends and family for viewing the site and giving feedback.