# DevOps Trial Day

## The Mission

Your mission for this is to deploy the application in `/deploy/` to OpenShift.

The application prints some technical information and then calculates Pi to a certain accuracy. As usual in our field, let's not think too much about the actual code and let's just pretend that's what management wanted.

How you deploy it is entirely up to you, use all the tools you can think of. You could use OpenShift's app examples, craft your own resource configuration file or leverage some sort of serverless-style deployments.

At it's most basic version you should end up with a URL that will serve the application and calculate Pi for the visitor.

What follows are some bonus points to be achieved. Note that the list is not exhaustive, so as long as the primary objective has been achieved, feel free to go off script and show off whatever cool DevOps tricks you have up your sleeves!

It's unlikely that you will finish with all of the bonus points in time, so focus on the ones you're feeling confident with.

Finally, this isn't a test of having something that works perfectly and is production ready. We're more interested in what approaches you have made, what you have struggled with and how you have overcome obstacles.

Keep in mind, going down a route, failing and then deciding that that is the wrong way of doing things is perfectly fine and an everyday thing - explain how and why you've made your decisions at the end of the day in the debrief.

### Bonus points:
- TLS with HTTP -> HTTPS redirect
- Centralised logs of the app to see what it's doing
- Capturing the errors of the application and notifying the responsible people (who?)
- Dashboard showing application health and metrics
- Secure configuration at the network level
- Secure configuration at the software level
- Documentation
- Architecture diagram
- CI Pipeline (with different steps: build, test, analyse)
- Automatic deploys when code is merged to master
- Automatic deploys on new branches / pull requests
- Caching that caches the apps' output for the correct period of time
- Scaling that in some way survives load testing (e.g. using apachebench)

## The App

Requirements/instructions can come in different forms and are usually pretty vague, so here's one example...:

> You will need a python 3 environment. Then install the requirements from the file. Afterwards simply execute the app.py file to run the server. Oh, and you can run unittests with pytest!
