from django.shortcuts import render, reverse

from .mixins import OrganisorAndLoginRequiredMixin

from django.views import generic
from leads.models import Agent
from .forms import AgentModelForm

class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = "agents/agent_list.html"
    
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
        template_name = "agents/agent_detail.html"

        def get_queryset(self):
            organisation = self.request.user.userprofile
            return Agent.objects.filter(organisation=organisation)
        
        context_object_name = 'agent'
            

class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"

    def get_queryset(self):
            organisation = self.request.user.userprofile
            return Agent.objects.filter(organisation=organisation)

    def get_success_url(self):
        return reverse("agents:agent-list")
         
    
    
class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    
    def get_queryset(self):
        return Agent.objects.all()
         
    def get_success_url(self):
        return reverse("agents:agent-list")
