name: Bug Report
description: Report a bug to help improve the swarm
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: "### 🐞 Bug Details"
  - type: textarea
    id: description
    attributes:
      label: Description
      description: What happened?
    validations:
      required: true
