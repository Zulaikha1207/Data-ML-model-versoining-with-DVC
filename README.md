# Iterative tools for Data Scientists

This repo covers the [Iterative.ai course](https://learn.iterative.ai/). The aim of the corse is to learn how to create flexible and effective pipeline to get machine learning projects into production efficiently and reproducible. 

## Creating structure in data projects

When starting data projects, we generally follow an ad-hoc workflow for conducting projects. Begin with local Python or R notebooks and train models on a local machine. For small projects, this works well: there is little overhead to worry about, and we can iterate quickly.

However, at later stages, it might prove beneficial to move towards a more structured approach. This holds especially true when working on a complex project with multiple team members. We might want to work on the same model simultaneously without having to worry about versioning. Or we need to ensure reproducibility across different machines. At this stage, tools and best practices for data science start to really make sense.

### Some best practices to follow:

- Project structure: follow a standard project/repository structure to improve collaboration (you can use cookiecutter for this or simply look up an established standard repo structure and follow that)
- Dependency management: Create a virtual env for each project. Instead of pip, you can also use other dependency mangement tools such as Poetry 
- Documentation: Always have a resourceful README.md file that explains how to run the code and gives relevant information about the project
- Versoning: Use Git (obviously) for code versioning. Just like code, in data science projects, data changes (highly dynamic) and it's important to know which version of data produced which model/ metrics
- Automation and pipeline: EDA with Jupyter Notebooks but create modular scripts for each step in the ML lifecyle
