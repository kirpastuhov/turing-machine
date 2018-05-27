from django.shortcuts import render
from .own import Tape, State
from .models import Data, Step
from django import template
import ast
# Create your views here.

def index(request):
    return render(request, 'machine/index.html')

def t_m(request):
		user_programm = {
		"q1" : {
		's_0': ["q0", '1', 'L'],
		'0': ["q0", '1', 'L'],
		'1': ["q0", '1', 'L'],
		'2': ["q0", '1', 'L'],
		},
		"q2" : {
		's_0': ["q0", '1', 'L'],
		'0': ["q0", '1', 'L'],
		'1': ["q0", '1', 'L'],
		'2': ["q0", '1', 'L'],
		},
		"q3" : {
		's_0': ["q0", '1', 'L'],
		'0': ["q0", '1', 'L'],
		'1': ["q0", '1', 'L'],
		'2': ["q0", '1', 'L'],
		},
		}
		new_tape = Tape()
		new_tape.tape = request.POST.get('tape').split(',')
		new_state = State()

		if request.POST.get('iter'):
			iterations = request.POST.get('iter')
		else: iterations = 1000

		k = 1
		context = {}
		alphabet = ['0', '1', '2', 's_0']

		if 'File' in request.POST:
			try:
				with request.FILES['Prog'] as f:
					f = f.open().read().decode().strip()
					user_programm = ast.literal_eval(f)
			except:
				context["input_file_err"] = "Bad File"
				return render(request, 'machine/index.html', context)


			context["a"] = (',').join(user_programm["q1"]["s_0"])
			context["b"] = (',').join(user_programm["q1"]["0"])
			context["c"] = (',').join(user_programm["q1"]["1"])
			context["d"] = (',').join(user_programm["q1"]["2"])
			context["e"] = (',').join(user_programm["q2"]["s_0"])
			context["f"] = (',').join(user_programm["q2"]["0"])
			context["g"] = (',').join(user_programm["q2"]["1"])
			context["h"] = (',').join(user_programm["q2"]["2"])
			context["i"] = (',').join(user_programm["q3"]["s_0"])
			context["j"] = (',').join(user_programm["q3"]["0"])
			context["k"] = (',').join(user_programm["q3"]["1"])
			context["l"] = (',').join(user_programm["q3"]["2"])
			return render(request, 'machine/index.html', context)




		if 'Full' in request.POST:

			user_programm["q1"]["s_0"] = request.POST.get('q1-s_0').split(',')
			user_programm["q1"]["0"] = request.POST.get('q1-0').split(',')
			user_programm["q1"]["1"] = request.POST.get('q1-1').split(',')
			user_programm["q1"]["2"] = request.POST.get('q1-2').split(',')

			user_programm["q2"]["s_0"] = request.POST.get('q2-s_0').split(',')
			user_programm["q2"]["0"] = request.POST.get('q2-0').split(',')
			user_programm["q2"]["1"] = request.POST.get('q2-1').split(',')
			user_programm["q2"]["2"] = request.POST.get('q2-2').split(',')

			user_programm["q3"]["s_0"] = request.POST.get('q3-s_0').split(',')
			user_programm["q3"]["0"] = request.POST.get('q3-0').split(',')
			user_programm["q3"]["1"] = request.POST.get('q3-1').split(',')
			user_programm["q3"]["2"] = request.POST.get('q3-2').split(',')

			context["a"] = (',').join(user_programm["q1"]["s_0"])
			context["b"] = (',').join(user_programm["q1"]["0"])
			context["c"] = (',').join(user_programm["q1"]["1"])
			context["d"] = (',').join(user_programm["q1"]["2"])
			context["e"] = (',').join(user_programm["q2"]["s_0"])
			context["f"] = (',').join(user_programm["q2"]["0"])
			context["g"] = (',').join(user_programm["q2"]["1"])
			context["h"] = (',').join(user_programm["q2"]["2"])
			context["i"] = (',').join(user_programm["q3"]["s_0"])
			context["j"] = (',').join(user_programm["q3"]["0"])
			context["k"] = (',').join(user_programm["q3"]["1"])
			context["l"] = (',').join(user_programm["q3"]["2"])



			context["tape"] = []
			while k <= int(iterations) and new_state.state != 'q0':
				if k == 999:
					context["iter_err"] = "Out of iterations"

				if new_tape.tape[new_tape.head_position] not in alphabet:
					context["char_err"] = 'Bad Char'
					break

				elif new_tape.tape[new_tape.head_position] in alphabet:
					current_obj = new_tape.tape[new_tape.head_position]

				current_prog_line = user_programm[new_state.state]

				try:
					new_tape.write(new_tape.head_position, current_prog_line[current_obj][1])
				except IndexError:
					context["mat_err"] = 'Bad task'
					break

				if new_tape.write(new_tape.head_position, current_prog_line[current_obj][1]) == False:
					context["err"] =  'Bad char'
				new_tape.move_head(current_prog_line[current_obj][2])
				new_state.change_state(current_prog_line[current_obj][0])
				tape = ('').join(new_tape.tape)
				context["tape"].append(tape)
				k = k + 1

				print(context)

			return render(request, 'machine/index.html', context)


		if 'Step' in request.POST:
			user_programm["q1"]["s_0"] = request.POST.get('q1-s_0').split(',')
			print(request.POST.get('q1-s_0').split(','))
			user_programm["q1"]["0"] = request.POST.get('q1-0').split(',')
			user_programm["q1"]["1"] = request.POST.get('q1-1').split(',')
			user_programm["q1"]["2"] = request.POST.get('q1-2').split(',')

			user_programm["q2"]["s_0"] = request.POST.get('q2-s_0').split(',')
			user_programm["q2"]["0"] = request.POST.get('q2-0').split(',')
			user_programm["q2"]["1"] = request.POST.get('q2-1').split(',')
			user_programm["q2"]["2"] = request.POST.get('q2-2').split(',')

			user_programm["q3"]["s_0"] = request.POST.get('q3-s_0').split(',')
			user_programm["q3"]["0"] = request.POST.get('q3-0').split(',')
			user_programm["q3"]["1"] = request.POST.get('q3-1').split(',')
			user_programm["q3"]["2"] = request.POST.get('q3-2').split(',')

			context["a"] = (',').join(user_programm["q1"]["s_0"])
			context["b"] = (',').join(user_programm["q1"]["0"])
			context["c"] = (',').join(user_programm["q1"]["1"])
			context["d"] = (',').join(user_programm["q1"]["2"])
			context["e"] = (',').join(user_programm["q2"]["s_0"])
			context["f"] = (',').join(user_programm["q2"]["0"])
			context["g"] = (',').join(user_programm["q2"]["1"])
			context["h"] = (',').join(user_programm["q2"]["2"])
			context["i"] = (',').join(user_programm["q3"]["s_0"])
			context["j"] = (',').join(user_programm["q3"]["0"])
			context["k"] = (',').join(user_programm["q3"]["1"])
			context["l"] = (',').join(user_programm["q3"]["2"])



			while k <= int(iterations) and new_state.state != 'q0':
				if k == 999:
					context["iter_err"] = "Out of iterations"

				if new_tape.tape[new_tape.head_position] not in alphabet:
					context["char_err"] = 'Wrong alphabet'
					print()
					break

				elif new_tape.tape[new_tape.head_position] in alphabet:
					current_obj = new_tape.tape[new_tape.head_position]

				current_prog_line = user_programm[new_state.state]

				try:
					new_tape.write(new_tape.head_position, current_prog_line[current_obj][1])
				except IndexError:
					context["mat_err"] = 'Bad task'
					break

				if new_tape.write(new_tape.head_position, current_prog_line[current_obj][1]) == False:
					context["err"] =  'Bad Char'
					break
				new_tape.move_head(current_prog_line[current_obj][2])
				new_state.change_state(current_prog_line[current_obj][0])

				Data(tape=('').join(new_tape.tape), iteration=k, state=str(new_state.state), task=('').join(current_prog_line[current_obj]), head_position=new_tape.head_position).save()
				k = k + 1
			data = Data.objects.all()
			step = Step.objects.get()

			print(list(data))
			if list(data) == []:
				context['bad_tape_task'] = 'Bad tape or task'
				return render(request, 'machine/index.html', context)
			else:
				try:
					context["step"] = data.get(iteration=step.step)
					step.step = step.step + 1
					step.save()
				except Data.DoesNotExist:
					context["finished"] = 'Задание завершено'
					context["step"] = data.get(iteration=(step.step-1))
				return render(request, 'machine/index.html', context)

		if 'Clear' in request.POST:
			Data.objects.all().delete()
			a = Step.objects.get()
			a.step = 1
			a.save()
			return render(request, "machine/index.html")
