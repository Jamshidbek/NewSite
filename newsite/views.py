from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Region, District
from .forms import RegionForm, DistrictForm


def region_list(request):
    regions = Region.objects.all().order_by('name')
    return render(request, 'newsite/region_list.html', {'regions': regions})


def region_detail(request, pk):
    region = get_object_or_404(Region, pk=pk)
    region_count = District.objects.filter(region=pk).count()
    return render(request, 'newsite/region_detail.html', {'region': region, 'region_count': region_count})


def region_new(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            region = form.save(commit=False)
            region.changed_date = timezone.now()
            region.save()
            return redirect('region_detail', pk=region.pk)
    else:
        form = RegionForm()
    return render(request, 'newsite/region_edit.html', {'form': form})


def region_edit(request, pk):
    region = get_object_or_404(Region, pk=pk)
    if request.method == "POST":
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            region = form.save(commit=False)
            region.changed_date = timezone.now()
            region.save()
            return redirect('region_detail', pk=region.pk)
    else:
        form = RegionForm(instance=region)
    return render(request, 'newsite/region_edit.html', {'form': form})


def district_list(request, pk):
    districts = District.objects.filter(region=pk).order_by('name')
    return render(request, 'newsite/district_list.html', {'districts': districts, "pk": pk})


def district_detail(request, pk):
    district = get_object_or_404(District, pk=pk)
    return render(request, 'newsite/district_detail.html', {'district': district, 'pk': district.region.id})


def district_new(request, pk):
    if request.method == "POST":
        form = DistrictForm(request.POST)
        if form.is_valid():
            district = form.save(commit=False)
            district.changed_date = timezone.now()
            district.region = get_object_or_404(Region, pk=pk)
            district.save()
            return redirect('district_detail', pk=district.pk)
    else:
        form = DistrictForm()
    return render(request, 'newsite/district_edit.html', {'form': form})


def district_edit(request, pk):
    district = get_object_or_404(District, pk=pk)
    if request.method == "POST":
        form = DistrictForm(request.POST, instance=district)
        if form.is_valid():
            district = form.save(commit=False)
            district.changed_date = timezone.now()
            district.save()
            return redirect('district_detail', pk=district.pk)
    else:
        form = DistrictForm(instance=district)
    return render(request, 'newsite/district_edit.html', {'form': form})