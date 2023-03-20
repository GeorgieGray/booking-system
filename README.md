# lettuce Eat

![devices](https://i.imgur.com/6dBgRra.png)

[All About Dinos](https://georgiegray.github.io/all-about-dinos/) is an educational website about dinosaur history, intended for children. It provides a jumping-off point for children to begin learning about dinosaurs.

The content is kept relatively concise and playful to keep it interesting for the target demographic. All About Dinos does not provide everything there is to know about dinosaurs, it's more intended as a starting point to pique the interests of future dinosaur enthusiasts.

The website consists of four main areas:
- The home page (or introduction)
- The dinosaur index
- The dinosaur profile page(s)
- The dino facts newsletter

There are 19 pages in total, including 15 dinosaur profiles.

The website is hosted using GitHub Pages, see it here:  
https://georgiegray.github.io/all-about-dinos/

## Table of Contents
- [Project Requirements](#project-requirements)
  - [User Experience](#user-experience)
  - [Development](#development)
  - [Deployment & Version Control](#deployment--version-control)
- [Target Demographic](#target-demographic)
- [User Stories](#user-stories)
- [Features](#features)
- [Technology](#technology)
- [Project Structure](#project-structure)
- [Design](#design)
  - [Colour Palette](#colour-palette)
  - [Typography](#typography)
- [Local Development](#local-development)
- [Deployment](#deployment)
- [Testing](#testing)
  - [Issues](#issues)
  - [Third-Party](#third-party)
    - [W3C HTML Validator](#w3c-html-validator)
    - [W3C CSS Validator](#w3c-css-validator)
    - [Lighthouse](#lighthouse)
- [Content](#content)
  - [Editorial](#editorial)
  - [Media](#media)
- [Citations & Credits](#citations--credits)


## Project Requirements

### User Experience
- Main navigation menu & structured website layout
- Considerations for accessibility
- Sensible information hierarchy
- Consist content style & use of colour
- Must include a media element: audio or video

### Development
- At least three unique pages
- Passes the W3C HTML Validator
- Passes the W3C CSS Validator
- Suitable use of images: no pixelation or deformation
- External links should open in a seperate tab
- All internal links must work
- HTML element usage should be semantically correct
- No placeholder content allowed
- Intuitive website navigation

### Deployment & Version Control
- Should be deployed to a cloud hosting platform
- Use Git & GitHub as version control
- No commented out code in Git

### Maintainability
- Write a README.md
  - Project description
  - Screenshots
  - User value
  - Deployment
  - Provide references & give credit for anything not original
- Use an intuitive project structure for easy file discovery
- No inline CSS
- Good code readability & formatting, and naming consitency
- Locate asset files together (CSS, Images, etc)

## Target Demographic
- Children aged 7+
  - All About Dinos is a text heavy website with a handful of illustrations which provide additional context about the historical information.
  - Children must understand the concept of a paragraph, be able to understand context and use pictures as an aid to better understand words which are new to them. My research suggests most children have these skills developed starting at the age of 7.
- Any adult without basic dinosaur history knowledge
  - Although lacking the kinds of deep information adults will be accustomed to in their regular daily reading, any adult may find this website useful as a light introduction to the topic.
- Geographical location is unimportant, but the website is only provided in English so the demographic will be limited to English speakers.

## User Stories

- As a user, I want to learn the names of specific dinosaurs
- As a user, I want to learn about the history of specific dinosaurs
- As a user, I want to learn about the types/categories of dinosaurs
- As a user, I want to learn about the time periods when dinosaurs existed
- As a user, I want to learn about the geography of the earth during the time of dinosaurs
- As a user, I want to learn why dinosaurs no longer exist
- As a user, I want to learn about what dinosaurs ate
- As a user, I want to look at illustrations of dinosaurs
- As a user, I want to sign up to a dinosaur facts newletter
- As a user, I want to find the All About Dinos social media accounts

## Features
### Header/navigation bar
- Website logo which can be clicked to return to the home page
- Primary navigation links to the home page and the dinosaur index
- Mobile-friendly navigation menu, hidden behind hamburger icon. The text is much larger to make it easier to use via touch controls on a small screen.

![header1](https://i.gyazo.com/8a9f06706a8ebed7bb137e45e49ea3b0.png)  
![header2](https://i.imgur.com/j7VvhjO.gif)

### Footer
- Provides links to social media accounts for All About Dinos
- Social media links are commonly put in this place on websites, so the user will intuitively know where to find them.

![footer](https://i.gyazo.com/95afd0ce6e44c673b73023c6a10c5ac4.png)

### Dinosaur Card
The dinosaur card is intended to prompt the user to want to learn more about a particular dinosaur based on their name or appearance.

The card includes:
- Dinosaur illustration
- Dinosaur name
- Link to the profile page for that dinosaur

The card zooms the image, and changes the learn more text decoration to imply to the user that the component is interactable.

![card](https://i.imgur.com/8MLNR8S.gif)  

### Dinosaur Mosaic
The dinosaur mosaic is a collection of dinosaur cards arranged in a masonry grid style, implemented using CSS grid. This component is the hero header for the home page. It showcases what I think are the most interesting dinosaurs, and is intended to capture the interest of those who land on the home page for the first time.  

As the viewport size shrinks, the mosaic arranges itself to make best use of the screen real-estate while still staying true to the intent of the feature. See second example below.  

#### Primary arrangement
![mosaic1](https://i.gyazo.com/8c11c9de6f740e2f6b95b27d13025049.jpg)  

#### Secondary arrangement
![mosaic2](https://i.gyazo.com/7323edee0c2b135a062a6fc5f4da2031.jpg)

### Types of Dinosaur
- Explains the types/categories of dinosaurs, and how they're differentiated  
![what](https://i.gyazo.com/b079750fbc876803120ac20ca660b188.png)

### Dinosaur Time Periods
- Provides high-level information about dinosaur time periods
- Explains that dinosaurs existed within the Mesozoic era
- The three periods are: Triassic, Jurassic and Cretaceous  
![when](https://i.gyazo.com/2897b4a66141861915efbb449792191c.png)

### Dinosaur Geography
- Information about where dinosaurs existed, and where they travelled.
- Includes an illustration of Pangea, a single super-continent where all dinosaurs coexisted before contentinental drift created todays earth.  
![where](https://i.gyazo.com/a1dca91d41031db4fe527d8761650494.png)
![pangea](https://i.gyazo.com/c40a89835081284eabb8ac6bda22e7ce.png)

### The End of the Dinosaurs
- An explanation of how the dinosaurs came to their demise
- Youtube video by popular education channel: Kurzgesagt
- The channel provides factual information but conveys it using a fun and playful art style, making it approachable for children.
  
![end](https://i.gyazo.com/888b36c738c597d338acfb668c9394f8.png)

### Dinosaur Index
- A non-exhaustive alphabetically ordered list of dinosaurs
- The familiar dinosaur card style from the home page makes an appearance here, but arranged in a different style with no "hero" card.
- This page is intended to behave as a list or "index" for the available dinosaur information available on the website.
- When clicked the cards link to each dinosaurs unique profile page including further historical information.

![dinos](https://i.gyazo.com/38c8a2e0156855dfe3fcf6db3f74ae4d.png)

### Dinosaur Profile Page(s)
- The name and an illustration of the dinosaur
- An introduction paragraph to set the scene
- Two or more additional sub-sections providing additional facts and information about the dinosaur. These include diet, appearance, temperament & nature, their height or weight, and some random trivia facts.
- There are 15 unique dinosaur profile pages

![profile](https://i.gyazo.com/5f4513155cf23076cb6e68bf30f7a3c1.png)

### Dinosaur Facts Newsletter

- Allows the user to sign-up to the dino facts newsletter
- Every 2 weeks, the user will recieve new information via email
- Secondary purpose is as a marketting aid, a newsletter reminds the user of the websites existence and may prompt them to return later

#### Sign-up form
- A small content area providing the user with context, it explains what the newsletter is and encourages the user to sign up
- A form with three inputs: first name, second name, email.
- A button to submit their details and sign up to the newsletter

![sign up](https://i.gyazo.com/ab0a8533c510dd7e732a28975f126170.png)

#### Thank you page
- A brief thank you message, I want the user to experience positive emotion after signing up for the newsletter
- The page includes a pun and a playful image
- The information presented on this page confirms with the user what action they have just undertaken, and what concequences the action will have

![thank-you](https://i.gyazo.com/fc214f4799575d3c4d4186cd1c70adf9.png)

## Technology

- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/CSS)

This project has no libraries or other code dependencies. All code is my own.

## Project Structure

### Assets

There is a folder in the root `/assets` which is the home for all non-html files.

This folder contains two child folders:
- `/assets/css`: All CSS files, for every page
- `/assets/images`: Images used across the website

### Page structure (HTML files)

All HTML files live in a folder bearing the name of that page, the HTML files themselves and are named `index.html`. Most web servers understand `index.html` to be the default file to display when a folder is requested, and I can use this to my advantage to create more user-friendly URL structures without exposing technical details like the file type.

For example `/all-about-dinos/dinosaur.html` can instead be `/all-about-dinos/dinosaur`.

Having our pages in a folder structure lets us communicate the relationship or hierarchy of pages within our website. This allows us to produce easier to read, more memorable, intuitive, SEO friend semantic URLs. These convey the meaning of the page within the context of the website hierarchy.

For example `/all-about-dinos/iguanodon.html` can instead be `/all-about-dinos/dinosaur/iguanodon`. The iguanodon is a dinosaur, this is now conveyed by our URL structure. The list of all dinosaurs is available one-level up at `/all-about-dinos/dinosaur`. As the user navigates through the site and explores into a particular area, the URL structure behaves sort of like a breadcrumb. The breadcrumb makes it clear to the user when they have gone one-level deeper or one-level higher in the site hierarchy, or even if they have switched context completely to another part of the website.

In the next section, I'll explain what each folder is for.

#### Root `/`

The root contains the home page, the root of the website.

#### Dinosaur list `/dinosaur`

The dinosaur section of the website, including a list of all dinosaurs.

#### Dinosaur profile `/dinosaur/{dinosaur-name}`

The individual profile page of a dinosaur.

#### Facts newsletter sign-up `/facts`

The form to sign up for the dino facts newsletter

#### Facts newsletter thank you `/facts/thank-you`

The thank you page for a new newsletter subscriber.

## Design

### Colour Palette

Green is a thematic colour for dinosaurs. You will often see in media related to dinosaurs an abundance of green due to the fauna and overgrowth of the environments they inhabited. The shades of green were selected with the intention of adding flavour without distracting from the content.

The tertiary colour is not green, but instead is complimentary to the other colours in the palette. It pops when placed with them as the background.

![palette](https://i.imgur.com/o3pAJEh.png)

### Typography

I chose [Quicksand](https://github.com/andrew-paglinawan/QuicksandFamily) by [Andrew Paglinawan](https://andrewpaglinawan.com/). The font is distributed using [Google Fonts](https://fonts.google.com/specimen/Quicksand).

When choosing a font I looked for the following criteria:
- Fun or playful
- Easy to read

Quicksand belongs to the sans-serif family. [This article](https://www.adobe.com/creativecloud/design/discover/serif-vs-sans-serif.html) by Adobe makes an argument for why you might choose a sans-serif font over a serif one. [This article](https://www.impactplus.com/blog/sans-serif-vs-serif-font-which-should-you-use-when#:~:text=Sans%20Serif%20Fonts%20Say%20Modern%2C%20Approachable%2C%20and%20Clean&text=The%20clean%2C%20crisp%20lines%20of,which%20increases%20legibility%20for%20users.) by impactplus.com says much of the same, but makes a stronger argument for sans-serif being the family of choice for on-screen text, and for ease of reading.

![sample image](https://i.gyazo.com/24f9d8ba1815d11e98f07ac18253c8eb.png)

## Local Development

You will need `npm`, 5.2 or later.

To run the project locally:
1. Clone this GitHub repo
2. It should be cloned into a folder called `all-about-dinos`
3. From **outside** the folder, run: `npx serve`
4. Open a web browser at: `http://localhost:3000/all-about-dinos`

I've setup the local development environment this way so that paths match the structure from the GitHub pages hosted version. This is important because it provides you with additional confidence that something which works locally will work the same once it's deployed.

Example:
### Github Pages
> https://georgiegray.github.io/all-about-dinos/dinosaur/iguanodon/

### Local
> http://localhost:3000/all-about-dinos/dinosaur/iguanodon/

## Deployment
Deployment is automated using GitHub pages.

Each time a commit is pushed to the `master` branch of the repository at `https://github.com/GeorgieGray/all-about-dinos`, the change is automatically detected and immediately deployed using [GitHub Actions](https://github.com/features/actions).

You can see the deployment history here:  
https://github.com/GeorgieGray/all-about-dinos/actions

## Testing

### Methodology

1. Do each of the following actions using multiple browsers, namely: Chrome, Firefox, Safari, Edge
    1. Visit every page on the website, scanning and visually check for abnormalities
    2. Interact with every link and image on the website, confirm that they have loaded and are linking to the correct place. All images should have a descriptive alt attribute.
    3. Confirm that as the website resizes between responsive breakpoints that the website continues to work as expected in a number of resolutions and viewport sizes. It's important to do this check as some users will not use the website with their browser window fully expanded. The website must support all window and viewport sizes between our defined breakpoints.
    4. Check mobile viewport exclusive functionality such as the mobile navigation menu
    5. Submit the newsletter form, and confirm that the navigation to the thank-you page works as expected.
2. Using the chrome-dev-tools, emulate devices of various sizes and check for usability and styling abnormalities. 
    - Large desktop
    - Small desktop
    - Tablet
    - Large phone
    - Small phone
3. Review the dinosaur-specific profile content, confirm the correct content is displayed for each dinosaur.
4. Confirm that the social-media links work as expected.
5. Use the WebAIM Contrast Checker to validate that any new colours satisfy the accessibility contrast guidelines for WCAG AAA, across all text types.
6. Run each page through the W3C HTML & CSS validators to confirm everything is compliant and implemented correctly.
7. Run the Lighthouse performance, accessibility, best practice and SEO tests using the chrome-dev-tools.
8. Each time a change is introduced or a bug is fixed, repeat this testing strategy.

### Third-party

I've used a set of third-party testing utilities to check my conformance with the CSS and HTML specifications, and to test website performance.

#### W3C HTML Valdiator
Each page type has been validated using the W3C Nu HTML Checker. There are no errors, please find the results below.

- Home: https://validator.w3.org/nu/?doc=https%3A%2F%2Fgeorgiegray.github.io%2Fall-about-dinos
- Dinosaur index: https://validator.w3.org/nu/?doc=https%3A%2F%2Fgeorgiegray.github.io%2Fall-about-dinos%2Fdinosaur
- Dinosaur profile: https://georgiegray.github.io/all-about-dinos/dinosaur/triceratops
- Facts newsletter form: https://validator.w3.org/nu/?doc=https%3A%2F%2Fgeorgiegray.github.io%2Fall-about-dinos%2Ffacts%2F
- Facts thank-you page: https://validator.w3.org/nu/?doc=https%3A%2F%2Fgeorgiegray.github.io%2Fall-about-dinos%2Ffacts%2Fthank-you

#### W3C CSS Validator
Each page type has been validated using the W3C CSS Validation Service. There are no errors, please find the results below.

- Home: https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgeorgiegray.github.io%2Fall-about-dinos&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en
- Dinosaur index: https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgeorgiegray.github.io%2Fall-about-dinos%2Fdinosaur&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en
- Dinosaur profile: https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgeorgiegray.github.io%2Fall-about-dinos%2Fdinosaur%2Ftriceratops&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en
- Facts newsletter form: https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgeorgiegray.github.io%2Fall-about-dinos%2Ffacts&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en
- Facts thank-you page: https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fgeorgiegray.github.io%2Fall-about-dinos%2Ffacts%2Fthank-you&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en

#### Lighthouse

I used the Lighthouse performance, accessibility, best practices and SEO tests to test and tune my website.

##### Desktop
![desktop lighthouse result](https://i.imgur.com/aFQvQsY.gif)  
Apparently if you get all 100s, you get fireworks.

##### Mobile
![mobile lighthouse result](https://i.gyazo.com/49f14c96e3004fc4da3bf9b38576e65b.png)  
Mobile has more strict thresholds since generally the devices are less powerful and have a worse internet connection than desktop devices.

## Content

### Editorial

All editorial content on the website is aimed at children with basic reading comprehension skills. The information is kept playful, fun and concise. All information is accompanied by a picture to provide additional context.

This content is not my own, the majority of the content is borrowed from `https://kids.nationalgeographic.com/animals/prehistoric`. Where content wasn't available for a dinosaur I wanted to include in the website, it was constructed using a collection of different sources.

All credit is given in the [Citations & Credits](#citations--credits) section.

### Media
When choosing media for the website, I looked for images which satisifed the following criteria:
- Hisorically accurate
- Not scary: dinosaurs can be violent creatures, but I didn't want this to deter children from learning about them
- Shows dinosaurs in their natural habitat: dinosaurs are often shown in museums, as fossils and fictionally in non-natural locations. I wanted to avoid these types of images to better represent the dinosaurs as they lived at the time of their existance.
- Illustrutive art style where possible, rather than photo-realistic - but still anatomically accurate.
- Colourful & bright
- Non-violent
- Consistent in style

This content is not my own. All credit is given in the [Citations & Credits](#citations--credits) section.

## Citations & Credits

### Images
#### Misc
- Logo


### Content


#### Editorial
