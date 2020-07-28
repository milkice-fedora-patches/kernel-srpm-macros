Name:           kernel-srpm-macros
Version:        1.0
Release:        2%{?dist}
Summary:        RPM macros that list arches the full kernel is built on
# This package only exist in Fedora repositories
# The license is the standard (MIT) specified in
# Fedora Project Contribution Agreement
# and as URL we provide dist-git URL
License:        MIT
URL:            https://src.fedoraproject.org/rpms/kernel-srpm-macros
Source0:        macros.kernel-srpm
BuildArch:      noarch


%description
This packages contains the rpm macro that list what arches
the full kernel is built on.
The variable to use is kernel_arches.

%prep
# nothing to do


%build
# nothing to do


%install
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d
install -p -m 0644 -t %{buildroot}/%{_rpmconfigdir}/macros.d %{SOURCE0}
%if 0%{?rhel} >= 8
  sed -i 's/^%kernel_arches.*/%kernel_arches x86_64 s390x ppc64le aarch64/' \
    %{buildroot}/%{_rpmconfigdir}/macros.d/macros.kernel-srpm
%endif


%files
%{_rpmconfigdir}/macros.d/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Troy Dawson <tdawson@redhat.com> - 1.0-1
- Initial build

