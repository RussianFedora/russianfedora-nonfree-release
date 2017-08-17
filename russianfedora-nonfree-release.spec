#define repo free
%define repo nonfree
#define repo fixes

Name:           russianfedora-%{repo}-release
Version:        7
Release:        1.R
Summary:        Russian Fedora (%{repo}) Repository Configuration

Group:          System Environment/Base
License:        BSD
URL:            http://russianfedora.org
Source0:        RPM-GPG-KEY-russianfedora-%{repo}-fedora
Source1:        russianfedora-%{repo}.repo
Source2:        russianfedora-%{repo}-updates.repo
Source3:        russianfedora-%{repo}-updates-testing.repo
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

# If apt is around, it needs to be a version with repomd support
Conflicts:      apt < 0.5.15lorg3

%if %{repo} == "nonfree"
Requires:       russianfedora-free-release >= %{version}

%description
Russian Fedora repository contains open source and other distributable software for
Fedora. It based on Tigro repository.

This package contains the Russian Fedora GPG key as well as Yum package manager
configuration files for Russian Fedora's "nonfree" repository, which holds
software that is not considered as Open Source Software according to the
Fedora packaging guidelines. 
%endif

%if %{repo} == "fixes"
%description
Russian Fedora repository contains open source and other distributable software for
Fedora. It based on Tigro repository.

This package contains the Russian Fedora GPG key as well as Yum package manager
configuration files for Russian Fedora's "fixes" repository, which holds
fixes for software that already is in Fedora Everything or updates.
Fedora packaging guidelines.
%endif

%if %{repo} == "free"
%description
Russian Fedora repository contains open source and other distributable software for
Fedora. It based on Tigro repository.

This package contains the Russian Fedora GPG key as well as Yum package manager
configuration files for Russian Fedora's "free" repository, which holds only
software that is considered as Open Source Software according to the Fedora
packaging guidelines. 
%endif

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install

# Create dirs
install -d -m755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg  \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# GPG Key
%{__install} -Dp -m644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

# Yum .repo files
%{__install} -p -m644 %{SOURCE1} %{SOURCE2} %{SOURCE3} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d


%files
%defattr(-,root,root,-)
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/*


%changelog
* Thu Aug 17 2017 Arkady L. Shane <ashejn@yandex-team.ru> - 7-1.R
- update to EL7

* Wed Feb 22 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 6-2.R
- R: redhat-release, CentOS does not provide system-release

* Tue Oct 11 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 6-1.R
- initial build for EL
