%define name fence
%define version 1.26
%define release  %mkrel 2

Summary: fence The cluster I/O fencing system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
Patch0: fence-toolMakefile.patch.bz2
Patch1: fence-fencedMakefile.patch.bz2
License: GPL
Group: System
#Url: 
Buildrequires: cman-kernel ccs
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
fence The cluster I/O fencing system

%prep
%setup -q -n  %{name}-%{version}
%patch0 -p0
%patch1 -p0

%build
./configure --incdir=%{_includedir} \
	--kernel_src=/usr/src/linux \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--sbindir=%{_sbindir} \
	--sharedir=%{_datadir}/%name

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_initrddir}
%makeinstall DESTDIR=$RPM_BUILD_ROOT
mv -vf $RPM_BUILD_ROOT/etc/init.d/%{name}d $RPM_BUILD_ROOT%{_initrddir}/%{name}d

#%post
#%_post_service %{name}d

#%preun
#%_preun_service %{name}d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_initrddir}/%{name}d
%{_sbindir}/
%doc
%{_mandir}/man8/


