# Iterative tools for Data Scientists

This repo covers the [Iterative.ai course](https://learn.iterative.ai/). The aim of the corse is to learn how to create flexible and effective pipeline to get machine learning projects into production efficiently and reproducible. 

## Creating structure in data projects

When starting data projects, we generally follow an ad-hoc workflow for conducting projects. We probably begin with local Python or R notebooks and train models on a local machine. For small projects, this works well: there is little overhead to worry about, and we can iterate quickly.

However, at later stages, it might prove beneficial to move towards a more structured approach. This holds especially true when working on a complex project with multiple team members. We might want to work on the same model simultaneously without having to worry about versioning. Or we need to ensure reproducibility across different machines. At this stage, tools and best practices for data science start to really make sense.

Aside from making it easier for our colleagues to collaborate with us on our projects, it also makes it easier for us to revisit projects at a later stage. This is ideal when we want to run ML experiments at various points in time. In other words: what's good for collaboration is also good for experimenting and reproducibility in solo projects.

### Coding (software development) best practices

When starting with a prototype in a Jupyter Notebook, a project tends to grow organically in terms of usefulness and complexity. This becomes an ever-increasing hurdle for getting our teammates up to speed. The longer and more complex our code is, the more difficult it becomes to understand all of its ins and outs.

That's why we at Iterative think it's valuable to apply a methodological approach to our data science projects. While at first sight, it may seem like a hassle to worry about structure and set-up ("that's time I could be spending on fun data science projects!"), it ensures that our teammates can easily understand what we're working on. And vice versa.

So what are some of these best practices? We can look towards best practices from software development to improve the way we do coding in ML projects.

Here are the five principles we feel are most important:

- **Organize code into reusable units:** We should avoid code duplication and extract functionality into distinct modules, classes, and functions. The code we write for our projects should be loosely coupled and highly cohesive. This means that units of code should serve a specific function and that we should be able to change those units without affecting other ones.
- **Use Git for version control:** Git is the industry standard for version control. We should use it to track changes to our code so that we can compare versions over time and refer back to previous versions when needed.
- **Follow style guides:** As Joel Spolsky puts it: it's harder to read code than to write it. Following pre-determined style guides makes reading just a little easier. It becomes less troublesome to revisit code we have written in the past or to comprehend code written by our teammates.
- **Make dependencies and requirements explicit:** Software evolves over time. To ensure our code will still work in the future, we should specify which versions of dependencies and requirements to use. We can do so in a dedicated requirements file where we list all dependencies and their versions.
- **Testing:** We should test our code to ensure it does what it is supposed to do. Moreover, we should test our code to ensure it doesn't do anything beyond what we expect it to do.

As with any set of principles, these are guidelines rather than strict rules. There are situations where deviating from them is justified. Nevertheless, we feel that, generally speaking, our development process will improve when we stick to these principles. This makes collaboration easier and thus boosts our productivity in projects.

### Some best practices to follow:

- Project structure: follow a standard project/repository structure to improve collaboration (you can use cookiecutter for this or simply look up an established standard repo structure and follow that)
- Dependency management: Create a virtual env for each project. Instead of pip, you can also use other dependency mangement tools such as Poetry 
- Documentation: Always have a resourceful README.md file that explains how to run the code and gives relevant information about the project
- Versoning: Use Git (obviously) for code versioning. Just like code, in data science projects, data changes (highly dynamic) and it's important to know which version of data produced which model/ metrics
- Automation and pipeline: EDA with Jupyter Notebooks but create modular scripts for each step in the ML lifecyle
