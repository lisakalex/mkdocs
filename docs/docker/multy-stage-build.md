A Docker multi-stage build is a way to use **multiple `FROM` statements** in one Dockerfile so you can build your app in one stage and copy only the needed output into a smaller final image.[3][4]

## Why use it
It helps you keep the final image smaller because build tools, caches, and source files do not have to ship in the runtime image. It also improves security and often makes deployments faster because the final container contains less unnecessary software.[1][4][5]

## How it works
The usual pattern is:
- Stage 1: use a full build image to compile or package the app.
- Stage 2: use a lighter runtime image.
- Copy only the built artifact from stage 1 into stage 2.[4][1]

Example:
```dockerfile
FROM node:20 AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

## Simple meaning
Think of it like cooking in one kitchen and then serving only the finished dish on a clean plate. You keep the tools and mess out of the final serving container.[9][4]

## Main benefit
The biggest win is a smaller, cleaner final image, which is easier to ship and run.[1][4]

Sources
[1] Docker multi-stage build. An effective strategy to build production ... https://oluoch-odhiambo.medium.com/docker-multi-stage-build-an-effective-strategy-to-building-production-ready-docker-images-59fda6e94e0
[2] Docker Multistage builds explained in 8 minutes https://www.youtube.com/watch?v=V0kTEk7YA70
[3] Stop at a specific build stage https://docs.docker.com/build/building/multi-stage/
[4] Multi-stage builds - Docker Docs https://docs.docker.com/get-started/docker-concepts/building-images/multi-stage-builds/
[5] Understanding Multi-Stage Docker Builds https://www.blacksmith.sh/blog/understanding-multi-stage-docker-builds
[6] What Are Multi-Stage Docker Builds https://dev.to/pavanbelagatti/what-are-multi-stage-docker-builds-1mi9
[7] Learn Multi-Stage Builds Easy With Examples - Docker Development Tips & Tricks https://www.youtube.com/watch?v=vIfS9bZVBaw
[8] Day 3/40 - Multi Stage Docker Build - Docker Tutorial For Beginners - CKA Full Course 2024 https://www.youtube.com/watch?v=ajetvJmBvFo
[9] Understanding Docker Multistage Builds - Earthly Blog https://earthly.dev/blog/docker-multistage/
[10] 🧱 What is a Multi-Stage Build in Docker? https://dev.to/dpvasani56/what-is-a-multi-stage-build-in-docker-5cfl
