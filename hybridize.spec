%define	_source_filedigest_algorithm	md5
%define	_binary_filedigest_algorithm	md5

Summary: Generate an optimal rootfs hybridize list
Name: hybridize
Version: 1.1
Release: 1%{?dist}
Group: Applications/System
Source0: hybridize
BuildRoot: %{_tmppath}/%{name}-%{version}-root
License: Modified BSD
BuildArch: noarch
Packager: Daryl W. Grunau <dwg@lanl.gov>, Ben McClelland <ben@lanl.gov>
Prefix: %{_bindir}
Prefix: %{_mandir}

%description
hybridize generates a list of files and/or directories suitable for building
hybrid rootfs VNFS capsules.  The list is optimal in the sense that it
contains a minimal set of symbolic links back into the VNFS while ensuring that
entries from file reside in RAM.  The generated list is unique to the
/vnfs/root provided on the command line.


# no prep required
#%setup

# no build required
#%build

%install
umask 022
%{__rm} -rf $RPM_BUILD_ROOT

%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__install} -m 0750 %SOURCE0 $RPM_BUILD_ROOT%{_bindir}/hybridize

%{__mkdir_p} $RPM_BUILD_ROOT%{_mandir}/man1
pod2man --section=1 %SOURCE0 $RPM_BUILD_ROOT%{_mandir}/man1/hybridize.1

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0750,root,root) %{_bindir}/hybridize
%attr(0644,root,root) %{_mandir}/man1/hybridize.1.gz

%changelog
* Fri Jul 12 2013 Ben McClelland <ben@lanl.gov> 1.1-1
- Add exception list for fedora18 where top level directories are symlinks in OS

* Fri Apr 26 2013 Daryl W. Grunau <dwg@lanl.gov> 1.0-3
- Permit multiple kernel module subdirectories in the /vnfs/root.  Assign KVER
  to the newest of these which belong to an RPM providing a kernel; document this.
  Flag this /vnfs/root kernel so that PPSST will deterministicly select it.
- Generate a "universal" {S}RPM that can be built on/for any platform by
  setting the _source_filedigest_algorithm and _binary_filedigest_algorithm
  to the lowest common denominator (md5).

* Mon Apr 11 2011 Daryl W. Grunau <dwg@lanl.gov> 1.0-2
- Modified BSD license, released under the HPC operational suite.
- Support glob meta-characters in the whitelist; document this.

* Tue Nov 17 2009 Daryl W. Grunau <dwg@lanl.gov> 1.0-1
- First cut.
