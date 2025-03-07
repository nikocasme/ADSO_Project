from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.shortcuts import render
from django.contrib import messages  # Importar el sistema de mensajes
from django.http import JsonResponse

def appointment_calendar(request):
    appointments = Appointment.objects.all()
    events = []

    for appointment in appointments:
        events.append({
            "title": appointment.name,
            "start": str(appointment.date) + "T" + str(appointment.time),
        })

    return JsonResponse(events, safe=False)

def home(request):
    return render(request, 'students/home.html')  # Asegúrate de que esta plantilla exista


# Vista para mostrar la lista de citas
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'students/appointment_list.html', {'appointments': appointments})

# Vista para crear una nueva cita
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡La cita se ha guardado correctamente!")
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'students/appointment_form.html', {'form': form})

# Vista para actualizar una cita
from django.contrib import messages  # Importar mensajes si no lo hiciste antes

def appointment_update(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, "¡La cita ha sido actualizada correctamente!")
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'students/appointment_form.html', {'form': form})


# Vista para eliminar una cita
def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)  # Ahora sí está definido
    if request.method == "POST":
        appointment.delete()
        messages.success(request, "¡La cita ha sido eliminada correctamente!")
        return redirect('appointment_list')
    return render(request, 'students/appointment_confirm_delete.html', {'appointment': appointment})

def appointment_calendar_view(request):
    return render(request, 'students/appointment_calendar.html')