

class Technology(m.Model):
    name = m.TextField(unique=True)
    d = m.DateField(null=True, blank=True)
    finished_at =escription = m.TextField(null=True, blank=True)
    def __str__(self):
        return f"#{self.pk}:{self.name!r}"

class Project(m.Model):
    summary = m.TextField(null=True, blank=True)
    started_at m.DateField(null=True, blank=True)
    python = m.BooleanField()
    django = m.BooleanField()
    technologies = m.ManyToManyField(Technology, related_name="projects")

class Responsibility(m.Model):
    project = m.ForeignKey(Project, on_delete=m.CASCADE, related_name="responsibilities")
    summary = m.TextField()