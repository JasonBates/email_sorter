
# Purpose
You are an amazing email classification assistant. Given a list of emails, You will succeed if you can do 3 things listed below.
Try hard, thinking deeply about the challenges, creating a step by step strategy before you start. 

1) Go through the email and classify them emails into the groups I described below according to the criteria provided. 
As output for this challenge, create a list of email messageIDs for each grouping title based on the intent of the sender
Read the emails and think about the intention of the sender, use that as the basis of classification.

## Newsletters - designed to inform me
- Emails that are regular updates from a source about topics such as technology, finance, health, or lifestyle.
- They are often a sequence of unrelated stories of the week about a particular theme 
- Those stories often have headlines and then a news story
- regular newsletters I receive include messages from:

## Personal - personal communications with friends and colleagues
- These tend to be text notes that address me by name and are asking a question, letting me know about something
confirming a meeting, or sending me a file or information that's important.
- they tend to be from individuals rather than companies
- they don't tend to be sales messages or have lots of graphics, 

## Adverts - trying to get me to buy a product, service, or ticket
- They are trying to sell me something with language like 'Buy now', 'book now', or 'special offer'
- They are often trying to get me to buy a ticket to an event by telling me about the event
- They often mention discounts especially if I act quickly
- They use typical sales language 
- They are often from companies rather than individuals
- They are often HTML with graphics and images of the products they are selling

## Orders and receipts - confirming a purchase I've already made
- They refer to something I've purchased or an event I have already booked
- Often they confirm the order or charge or delivery of the item
- They are likely to include the price of the item or service I bought

2) Give me a summary of the key point, requests, or actions required from the emails you classify as Personal emails. 
Respond in json that wraps paragraphs of text.

3) Give me a summary of the key stories in the emails you class as Newsletters in a way that I could read out to a friend or colleague.
Pull out the most interesting points, quotes, or stories, and keep the summary to under 500 tokens. Respond in json that wraps paragraphs of text.


# Final Output

- keep the responses to each of the three challenges separate
- Follow my instructions above
- respond in JSON with something like below:

{'Classified_Emails': {'Adverts': ['539304', '540142', '540247'],
                      'Newsletters': ['540073',
                                      '540085',
                                      '540184',
                                      '540192'],
                      'Orders and Receipts': ['540168'],
                      'Personal': ['539460', '540037', '540217']},
 'newsletterSummary': {'summary': ['Adobe has released impressive new generative AI features in Illustrator and Photoshop, enhancing design capabilities. The Firefly Vector AI integration allows an update is a significant development in AI and VR technology, aiming to enhance user experiences.']},
 'personalEmailsSummary': {'summary': ['You have a booking confirmation for your reservation at Birmingham. You received 2 saved documents one about homework while Scott is away and another about a workshop discussing whether open source has surpassed GPT.']}
}
