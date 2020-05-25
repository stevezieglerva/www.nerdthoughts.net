---
layout: post
title: The World's Greatest Agile Management Chart
description: Cumulative flow diagrams
---


While cumulative flow diagrams came out of the Lean and Kanban communities, they can provide value on any software development project, even those using Scrum or waterfall. The diagram shows the count of work items in each work status over time. The diagrams are so popular because they show so many metrics about in a project in an easily digestable format. They can tell you:

- Is scope increasing?
- How long will the next work item take?
- When will the project be done?
- Where are the process bottlenecks?

I started my agile journey with Kanban. So, even though I mostly work with projects using Scrum, CFDs and Kanban principles (vizualize work, limit work-in-progress, reduce cycle time) are still near and dear to me. I find them most useful to verify PM or dev comments on project progress and the team's velocity.

Here are some typical CFD diagrams that I see with teams and how I interpret the diagrams.


## Typical CFD 
In this CFD, we can see the work grouped into the three typical phases: work to be done (To Do), work in progress (Doing), and completed work (Done).

![](/assets/img/cfd_typical.png)

My takes on the diagram are:
- Work is being finished! Not every team can say that. It's a little batchy but this team is delivery value to users.
- New work was added along the way. The work could have been new features, new bugs, or new O&M tasks. Unless this was a firm-fixed price contract, I wouldn't be that worried about it. My guess is the client/sponsor is happy with so much stuff getting to Prod.
- They are almost done. The green Done band has almost taken over the red To Do band.



## QA Bottleneck
In order to see bottlenecks in your processes, you need to be more granular in your Doing lane. I like to split out QA steps or record which enviroment (Dev, Test, Stage, Prod) an item is in. Another important status to measure is if something is ready for Prod, but not yet deployed. The CFD below also includes a QA status and Ready for Prod status.

![](/assets/img/cfd_bottleneck.png)

My takes on the diagram are:
- Early on, this team was doing a good job of getting items to Prod.
- Early on, the team was very consistent which is a stakeholder's dream! In the first month, the In Progress, QA, and Ready for Prod band have a consistent width.
- In mid-February, QA starts to become the bottleneck. 

## Death Spiral


## Perfect CFD

![](/assets/img/cfd_perfect.png)



