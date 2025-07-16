<script lang="ts" module>
	import AudioWaveformIcon from '@lucide/svelte/icons/audio-waveform';
	import BookOpenIcon from '@lucide/svelte/icons/book-open';
	import BotIcon from '@lucide/svelte/icons/bot';
	import ChartPieIcon from '@lucide/svelte/icons/chart-pie';
	import CommandIcon from '@lucide/svelte/icons/command';
	import FrameIcon from '@lucide/svelte/icons/frame';
	import GalleryVerticalEndIcon from '@lucide/svelte/icons/gallery-vertical-end';
	import MapIcon from '@lucide/svelte/icons/map';
	import Settings2Icon from '@lucide/svelte/icons/settings-2';
	import SquareTerminalIcon from '@lucide/svelte/icons/square-terminal';
	import Bolt from '@lucide/svelte/icons/bolt';
	import ShoppingCart from '@lucide/svelte/icons/shopping-cart';
	import { House } from '@lucide/svelte';
	import { Button } from '$lib/components/ui/button/index.js';
	import Building from '@lucide/svelte/icons/building';

	// This is sample data.
	const data = {
		user: {
			name: 'shadcn',
			email: 'm@example.com',
			avatar: '/avatars/shadcn.jpg'
		},
		teams: [
			{
				name: 'Telecomunicaciones San Antonio',
				logo: Building,
				plan: ''
			}
		],
		navMain: [
			{
				title: 'Realizar Nueva Venta',
				url: '/new-sale',
				icon: ShoppingCart,
				isActive: true,
				items: [
					{
						title: 'Realizar Venta',
						url: '/new-sale'
					},
					{
						title: 'Seleccionar Productos',
						url: '/new-sale/select-products'
					},
					{
						title: 'Seleccionar Servicios',
						url: '/new-sale/select-services'
					}
				]
			},
			{
				title: 'Gestionar Mi Negocio',
				url: '/mi-negocio',
				icon: Bolt,
				items: [
					{
						title: 'Gestionar Productos',
						url: '/gestionar-productos'
					},
					{
						title: 'Gestionar Servicios',
						url: '/gestionar-servicios'
					},
					{
						title: 'Gestionar Clientes',
						url: '/gestionar-clientes'
					},
					{
						title: 'Lista de Reposición',
						url: '/lista-reposicion'
					}
				]
			}
			/*
			{
				title: 'Documentation',
				url: '#',
				icon: BookOpenIcon,
				items: [
					{
						title: 'Introduction',
						url: '#'
					},
					{
						title: 'Get Started',
						url: '#'
					},
					{
						title: 'Tutorials',
						url: '#'
					},
					{
						title: 'Changelog',
						url: '#'
					}
				]
			},
			{
				title: 'Settings',
				url: '#',
				icon: Settings2Icon,
				items: [
					{
						title: 'General',
						url: '#'
					},
					{
						title: 'Team',
						url: '#'
					},
					{
						title: 'Billing',
						url: '#'
					},
					{
						title: 'Limits',
						url: '#'
					}
				]
			}*/
		] /*,
		projects: [
			{
				name: 'Design Engineering',
				url: '#',
				icon: FrameIcon
			},
			{
				name: 'Sales & Marketing',
				url: '#',
				icon: ChartPieIcon
			},
			{
				name: 'Travel',
				url: '#',
				icon: MapIcon
			}
		]*/
	};
</script>

<script lang="ts">
	import NavMain from './nav-main.svelte';
	import NavProjects from './nav-projects.svelte';
	import NavUser from './nav-user.svelte';
	import TeamSwitcher from './team-switcher.svelte';
	import * as Sidebar from '$lib/components/ui/sidebar/index.js';
	import type { ComponentProps } from 'svelte';

	let {
		ref = $bindable(null),
		collapsible = 'icon',
		...restProps
	}: ComponentProps<typeof Sidebar.Root> = $props();
</script>

<Sidebar.Root {collapsible} {...restProps}>
	<Sidebar.Header><TeamSwitcher teams={data.teams} /></Sidebar.Header>
	<Sidebar.Content>
		<NavMain items={data.navMain} />
		<!--<NavProjects projects={data.projects} />-->
	</Sidebar.Content>
	<Sidebar.Footer>
		<!--<NavUser user={data.user} />-->
	</Sidebar.Footer>
	<Sidebar.Rail />
</Sidebar.Root>
