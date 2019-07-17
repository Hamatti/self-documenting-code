# Self-Documenting Code

Finally, you can have code that truly is self-documenting.

**PLEASE NOTE!** Never use this code anywhere in real life. It's very hacky, it doesn't adhere to good software development practices and it will change your original source code, maybe in ways that breaks your code.

## Introduction & Motivation

This project started as a snarky comment in Twitter aimed towards the "Good code documents itself" trope. After I posted [the tweet](https://twitter.com/Hamatti/status/1150777986095955968), I started looking into the script more to see how I could make it better.

When I was young and in the beginning of my studies, there was a lot of discussion about documentation and especially code comments. Some of the more experienced developers who were already working in the industry were big proponents of "don't comment your code, good code is self-documenting" but I never really bought into the idea.

When I got older and gained more experience from the industry, I learned that my disagreement was justified. Documentation and comments should not be merely about **what** the code does, that can be to some extent inferred from the code if it's good and easy to read (which, doesn't happen that often in real projects). The documentation however should answer the **why** and explain the decisions, the tradeoffs and reasoning for what was build and why it was built like it was.

That **why** can never be inferred from the code itself because it holds no understanding of reasoning, it just executes commands and thus answers to the **what** or **how** questions.

And more than that, the "good code is self-documenting" attitude is hurtful for beginners entering the industry. They will look at their code and expect the minimum requirement to be perfect code that can be understood by anyone simply by looking at it. With years of experience in the industry, I have very rarely seen that happen: software is complex and understanding how it works requires a lot more than just looking at a piece of code.

Documenting your work (by whatever means you choose) is a sign of strenght, not weakness. We write documentation so it's easier for others (including future ourselves) to understand, to reason and to modify code. Making that harder by not documenting your code is doing a disservice to anyone who's gonna work on the codebase later.

## How it works?

To make code self-documenting, I created a function `document(docstring)` that finds the caller's name and filename, adds docstring into the correct position (first line of function body) and deletes the original call to `document`.

It uses hardcoded 4 spaces as the indentation level so if your original source code uses tabs or any other number of spaces than 4, it will break. There are probably a bunch of other places where it will break too (as you can find from this repository, there are no tests).
