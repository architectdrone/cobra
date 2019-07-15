# Project Cobra

This is a proof of concept for Cobra. I may come back later and make something better, however, for now this demonstrates what a fully functioning cobra-type project would look like.

## What is Cobra?

Cobra is an attempt to integrate coding and spreadsheets. The goal is to bring the power of scripting to the structure of spreadsheets.

## How does it work?

Every cell in a Cobra spreadsheet may have a script associated with it. When a cell with a script is changed, the script runs. Some data is passed to the script. The script then may edit other cells.

## How can I get started using this?

Create a new folder for your project, and edit the PROJECT_PATH variable in cobraMain. To add scripts, you need to have a scripts directory under the project directory. Any scripts you wish to add must be added here. 

## How does the Cobra command line work?

Here are the current commands:

- load: loads data from the project

- save: saves data from the project

- display: displays the spreadsheet

- put &lt;x&gt; &lt;y&gt; &lt;key&gt; &lt;value&gt;: puts &lt;value&gt; into the field &lt;key&gt; at &lt;x&gt;, &lt;y&gt;. Useful for debugging and testing purposes

- update &lt;x&gt; &lt;y&gt; &lt;value&gt;: updates the value of the cell at &lt;x&gt;, &lt;y&gt; to &lt;value&gt;, and runs any scripts associated with the cell

- script &lt;x&gt; &lt;y&gt; &lt;script&gt;: sets the script of &lt;x&gt;, &lt;y&gt; to &lt;script&gt;

## Why should I use this?

You shouldn't. Here's why:

- Stupidly insecure. Anyone could send you a cobra project file with malicious code in the scripts directory.

- Counter-intuitive scoping. Currently, all data is passed through a local variable into the environment where the script is run. This is kind of infuriating, and I would like to find a better way to do this.

- No protection against silliness. Infinite loops are not stopped, and it is up to the user to prevent them from occuring.

## Why would I want to use this in the future?

- You want more control over the functions in your spreadsheets. You think you can do better than the silly math majors at Microsoft who create Excel.

- You want complex events to occur when certain conditions are met on the spreadsheet.

- You really, really like writing macros, and wish there was an entire spreadsheet app that allowed you to do nothing but write macros.

## Why the name Cobra?

Because it was written in python, a python is a snake, and so is a cobra. :snake: