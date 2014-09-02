#define repo free
%define repo nonfree
#define repo fixes

Name:           russianfedora-%{repo}-release
Version:        21
Release:        1.R
Summary:        Russian Fedora (%{repo}) Repository Configuration

Group:          System Environment/Base
License:        BSD
URL:            http://russianfedora.org
Source0:        RPM-GPG-KEY-russianfedora-%{repo}-fedora
Source1:        russianfedora-%{repo}.repo
Source2:        russianfedora-%{repo}-updates.repo
Source3:        russianfedora-%{repo}-updates-testing.repo
Source4:        russianfedora-%{repo}-rawhide.repo
Source5:        russianfedora-%{version}-nonfree.xml.gz
Source6:        russianfedora-%{version}-nonfree-icons.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  libappstream-glib

Requires:       system-release >= %{version}

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
rm -rf $RPM_BUILD_ROOT

# Create dirs
install -d -m755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg  \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# GPG Key
%{__install} -Dp -m644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg

# Yum .repo files
%{__install} -p -m644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# AppStream metadata
DESTDIR=%{buildroot} appstream-util install %{SOURCE5} %{SOURCE6}

%clean
rm -rf $RPM_BUILD_ROOT


#%pre
#if [ -f /etc/yum.repos.d/russianfedora-%{repo}-pre-rawhide.repo ]; then
#    sed -i 's!enabled=1!enabled=0!g' /etc/yum.repos.d/russianfedora-%{repo}-pre-rawhide.repo
#fi


%files
%defattr(-,root,root,-)
%{_sysconfdir}/pki/rpm-gpg/*
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%attr(0644,root,root) %{_datadir}/app-info/xmls/*
%{_datadir}/app-info/icons/russianfedora-%{version}-nonfree/*.png

%changelog
* Tue Sep  2 2014 Arkady L. Shane <ashejn@russianfedora.ru> - 21-1.R
- update to RFRemix 21

* Mon Jun 23 2014 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 20-2.R
- include appstream metadata

* Fri Oct  4 2013 Arkady L. Shane <ashejn@yandex-team.ru> - 20-1.R
- update to RFRemix 20

* Fri Mar 29 2013 Arkady L. Shane <ashejn@yandex-team.ru> - 19-1.R
- update to RFRemix 19

* Mon Oct 22 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 18-2.R
- added debug and source mirrorlist url

* Wed Oct  2 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 18-1.R
- update to RFRemix 18

* Thu Feb 23 2012 Arkady L. Shane <ashejn@yandex-team.ru> - 17-1.R
- update to RFRemix 17

* Sun Sep 18 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 16-1.R
- update to RFRemix 16

* Fri Mar 18 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 15-1
- update to RFRemix 15

* Thu Oct 14 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 14-1
- stable release

* Wed May 19 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 13-1
- enable stable repos disable unstable

* Mon Mar 15 2010 Arkady L. Shane <ashejn@yandex-team.ru> - 13-0.1
- bump to 13

* Mon Nov  9 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 12-2
- fix updates repo

* Mon Nov  9 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 12-1
- update for RFRemix 12

* Sun Jan 11 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10-2
- add obsoletes for tigro-release
- fix repos files

* Fri Jan  9 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 10-1
- initial build for Fedora 10
