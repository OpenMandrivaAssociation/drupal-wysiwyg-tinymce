%define oname	tinymce

Name:		drupal-wysiwyg-tinymce
Summary:	TinyMCE editor for Drupal Wysiwyg module
Version:	3.5.6
Release:	2
License:	LGPLv2.1
Group:		Networking/WWW
URL:		http://www.tinymce.com/
Source0:	https://github.com/downloads/tinymce/%{oname}/%{oname}_%{version}.zip
Requires:	drupal-wysiwyg
Provides:	drupal-wysiwyg-editor
BuildArch:	noarch

%description
TinyMCE is a platform independent web based Javascript HTML WYSIWYG editor
control released as Open Source under LGPL by Moxiecode Systems AB.

TinyMCE has the ability to convert HTML TEXTAREA fields or other HTML elements
to editor instances. TinyMCE is very easy to integrate into other Content
Management Systems.

%prep
%setup -q -n %{oname}

%build

%install
%__install -d %{buildroot}%{_var}/www/drupal//sites/all/libraries/
cp -a . %{buildroot}%{_var}/www/drupal//sites/all/libraries/%{oname}
rm %{buildroot}%{_var}/www/drupal//sites/all/libraries/%{oname}/*.txt

%files
%{_var}/www/drupal//sites/all/libraries/%{oname}
%doc changelog.txt


%changelog
* Thu Aug 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.5.6-1
+ Revision: 813315
- update to 3.5.6

* Fri May 11 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.5.0.1-1
+ Revision: 798318
- imported package drupal-wysiwyg-tinymce

