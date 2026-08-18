class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_queue = deque(students)
        sandwich_queue = deque(sandwiches)
        rotation = 0
        while student_queue and rotation < len(student_queue):
            if student_queue[0] == sandwich_queue[0]:
                student_queue.popleft()
                sandwich_queue.popleft()
                rotation = 0
            else:
                student_queue.append(student_queue.popleft())
                rotation += 1
        return len(student_queue)