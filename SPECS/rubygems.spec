Summary	: Install rubygems 1.7.2
Name		: rubygems
Version		: 1.7.2
Release		: 1
License		: BSD
Group		: Applications
Source0 	: rubygems-1.7.2.tgz
BuildArch	: x86_64
BuildRoot	: /var/tmp/%{name}-buildroot
BuildRequires	: openssl, openssl-devel, gcc, zlib, zlib-devel, make 
BuildRequires	:  ruby >= 1.8.1
Prereq      	: /sbin/chkconfig, /bin/cp, /bin/mv
Prereq      	: sh-utils, textutils, /usr/sbin/groupadd, /usr/sbin/useradd
Requires	:  ruby >= 1.8.1

%description
Ruby-Gems

%prep
%setup

%build


%pre


%install
ruby setup.rb --destdir=%{buildroot}


%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/gem
/usr/lib/ruby/ruby/site_ruby/1.8/gauntlet_rubygems.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rbconfig/datadir.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/builder.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/command_manager.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/build_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/cert_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/check_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/cleanup_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/contents_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/dependency_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/environment_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/fetch_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/generate_index_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/help_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/install_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/list_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/lock_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/outdated_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/owner_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/pristine_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/push_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/query_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/rdoc_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/search_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/server_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/setup_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/sources_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/specification_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/stale_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/uninstall_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/unpack_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/update_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/commands/which_command.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/config_file.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/custom_require.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/defaults.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/dependency.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/dependency_installer.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/dependency_list.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/deprecate.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/doc_manager.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/errors.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/exceptions.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/ext.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/ext/builder.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/ext/configure_builder.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/ext/ext_conf_builder.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/ext/rake_builder.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/format.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/gem_openssl.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/gem_path_searcher.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/gem_runner.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/gemcutter_utilities.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/indexer.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/install_update_options.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/installer.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/installer_test_case.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/local_remote_options.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/mock_gem_ui.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/old_format.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/package.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/package/f_sync_dir.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/package/tar_header.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/package/tar_input.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/package/tar_output.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/package/tar_reader.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/package/tar_reader/entry.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/package/tar_test_case.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/package/tar_writer.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/package_task.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/platform.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/remote_fetcher.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/require_paths_builder.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/requirement.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/security.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/server.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/source_index.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/spec_fetcher.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/specification.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/test_case.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/test_utilities.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/text.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/uninstaller.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/user_interaction.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/validator.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/version.rb
/usr/lib/ruby/ruby/site_ruby/1.8/rubygems/version_option.rb
/usr/lib/ruby/ruby/site_ruby/1.8/ubygems.rb

%post

%preun

%changelog
* Mon Jun 14 2011 Arno Broekhof <arnobroekhof@gmail.com>
- Initial spec-file
