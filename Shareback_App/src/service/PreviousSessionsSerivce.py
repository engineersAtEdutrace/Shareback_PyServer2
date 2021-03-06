from Shareback_App.models import Sessions
from Shareback_App.src.adapter.dto.PreviousSessionsResponseDTO import SessionMetadata
from Shareback_App.src.service.base.BaseService import BaseService
from Shareback_App.src.util.DateFormatter import DateFormatter


class PreviousSessionsService(BaseService):
    LIMIT = 10

    def get_list(self, request_no):
        request_no -= 1;  # Converting to Index

        offset = PreviousSessionsService.LIMIT * request_no
        session_list = Sessions.objects.order_by('-timestamp')[offset: offset + PreviousSessionsService.LIMIT]
        dto_list = list()

        for session in session_list:
            session_dto = SessionMetadata()
            session_dto.set_session_id(session.session_id)
            session_dto.set_session_name(session.session_name)
            session_dto.set_date(
                DateFormatter.format(session.timestamp)
            )
            dto_list.append(session_dto)

        return dto_list
