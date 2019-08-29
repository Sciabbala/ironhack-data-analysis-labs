![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Reading About Statistic Concepts

## Introduction

In the future, you will need to understand deep statistical concepts by reading technical articles. As a training for that, it is interesting to start from here. Also, as we have limited time, this is a way to have some self guided learning to understand everything better and have a wider knowledge.

This week you will find some questions here that you will need to answer by documentating yourself. So you will do a different PR for each question (you are meant to answer the questions in different days). Don't hesitate to write as many text as you need and push images if you need them.

Remember for this lab: there is a right answer. But there is no perfect way to explain it (except for in a mathematical way, but this is another story).

## Challenges

### Challenge 1: What is the difference between expected value and mean?
You know both concepts but, is there a difference? Are they synonims? Start investigating. 

As a good reference (once you have looked for some information) you have   [this](http://expected.news/value2) article.

**Answer**
The expected values is a concept that is strictly related to probability and is related to the value that we expect a Random Variable X to take. In case all the different possibilities have the same weight and therefore probability to happen then the mean of those possibilities corresponds with the expected value but, for example, a weighted coin or dice that is more likely to fall on tails or roll on a 1 will not respect the mean.

The mean is also a mathematical concept that has nothing to do with probability per se.

### Challenge 2: What is the "problem" in science with p-values?
We have told you that a lot of scientifical investigations are based on p-values. The last week, Nature magazine published [an article](http://nature.social/statistical4) regarding the problem. Start digging on it!

Don't hesitate to use more articles if you want to :)

**Answer**
I believe that the main problem with the p-value is that, even though it sounds ugly, science is also a money-driven businesses. Researchers need to pay the bills and to do that they need grants, and to get grants they need to show positive results, because even though a study with a low significance STILL gives us very useful information that can be used in further research saying "I finished my research through grant X and I have found no/low significance" sounds worse than the opposite, especially when the objective is getting your paper published in science journals and impressing people who sometimes are less knowledgeable about the topic than the average researcher and therefore do not understand the nuances of something like the p-value.

We just collectively decided to set a hard-limit to divide "significance" and "non-significance" when the amount of things that could be factored in the results of a research are still outside of our complete grasp, thus invalidating research that could be actually valid and show useful information.

This pressures scientists and researcher to go as far as manipulate the data of their research (e.g. taking into consideration only certain parts) just to get the p-value under 0.05 because, at the end of the day, having a research that is considered significant (and thus valid) is usually the difference between paying the bills or be out of work.


### Challenge 3: Applying testing to a specific case: A/B testing.
A/B testing is a widely used tool to understand differences between two samples. It is a way to measure the impact of something we did: 
* A marketing campaign.
* A new feature in our application. 
* A new design in our application.
* A different flow in the User Experience flow.

To do this, is very important first to design our experiment. 
* We need to know how we are measuring the impact. If people has the behaviour we want with this new implementation.
* We choose a control group (people who doesn't have/see the new change) and the group which will see the new change. 
* We think about how much data do we need.
* We measure the difference between them.

One example:
Our application has a lot of mini-games. We want people to reach the games that we think are the best but the behaviour is not the expected, they don't reach them.

So we call a designer and after a lot of work he shows us a new design for our application: we will add a botton specific for that kinf of games inviting the users to click on it:

*Click here to discover cool games!*

We think it will work but can we be sure? So instead of implementing this new botton for all users, we implement it for 10% and we compare the results with the users that didn't have it. Is there a significant difference? Is our botton working?

**Answer**

I am not sure about the question but I suppose an A/B testing is the best option here. We simply take a sample and divide it into a control group that will see no change and a test group that will have the new button. We then wait until we have a collected enough data to go forward with our analysis and check if there was an improvement or not.


Read more about A/B testing with a couple of examples:

[Another example about Netflix here](http://select.video/artwork4)

[What happened to Basecamp](http://millions.social/tested7)

[An example with Python](http://math.social/tested3)

[A cool general explanation](http://arts.show/tested7)

## Deliverables
You need to submit a markdown file with the answers to the questions above. You can create a new `.md` file or directly edit the `README.md`.

## Submission
Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.