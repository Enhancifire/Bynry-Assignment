from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required
from datetime import datetime
from uuid import uuid4


@login_required
def create_request(request):
    form = ServiceRequestForm()
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            description = cleaned_data.get('description')
            request_type = cleaned_data.get('request_type')
            # attachments = request.FILES["attachments"]
            user = request.user

            req_id = str(uuid4())

            status = "OP"

            req = ServiceRequest(
                request_id=req_id,
                user=user,
                description=description,
                request_type=request_type,
                status=status,
                # attachments=attachments,
            )

            req.save()

            return redirect(f'/requests/{req_id}/')

        else:
            return render(request, "request/new_request.html", {'form': form})

    else:
        return render(request, "request/new_request.html", {'form': form})


def handle_file_upload(f, request_id):
    with open(f"{request_id}.png", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@login_required
def view_request(request, id):
    req = ServiceRequest.objects.get(pk=id)
    notes = req.requestnote_set.all()
    are_notes_available = len(notes) != 0

    return render(request, "request/view_request.html", {
        'req': req,
        'notes': notes,
        'are_notes_available': are_notes_available,
    })


@login_required
def view_all_requests(request):
    user = request.user
    service_requests = user.servicerequest_set.all()

    return render(request, "request/view_all_requests.html", {'requests': service_requests})
